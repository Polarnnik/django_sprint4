from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def posts():
    """Получение постов из БД"""
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )


def index(request):
    """Главная страница / Лента записей"""
    return render(request, 'blog/index.html', {'post_list': posts()[:5]})


def post_detail(request, id):
    """Отображение полного описания выбранной записи"""
    post = get_object_or_404(posts(), id=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Отображение публикаций категории"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    context = {'category': category,
               'post_list': posts().filter(category=category)}
    return render(request, 'blog/category.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return redirect('post_detail', pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
