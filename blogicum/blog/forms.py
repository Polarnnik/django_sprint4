from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'location', 'image', 'pub_date')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
