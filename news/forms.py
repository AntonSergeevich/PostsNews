from django.forms import ModelForm
from .models import Comment, Post
from django import forms
from django.contrib.auth.models import Group

# Создаём модельную форму
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'title', 'text', 'img']


class SignupForm(forms.Form):
    email = forms.EmailField(label='Почта')
    first_name = forms.CharField(max_length=30, label='Имя')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        user.save()