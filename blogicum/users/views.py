from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreationForm
from django.contrib.auth.models import User
from blog.models import Post
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.views.generic import DetailView

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration_form.html'

User = get_user_model();

class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object.posts.all(), self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
