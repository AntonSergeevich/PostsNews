from django.forms import ModelForm
from .models import Comment, Post


# Создаём модельную форму
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text', 'img']
