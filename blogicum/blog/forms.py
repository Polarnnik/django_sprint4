from django import forms
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'location', 'image', 'pub_date')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')
