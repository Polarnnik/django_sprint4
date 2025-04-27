from django import forms
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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

User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
