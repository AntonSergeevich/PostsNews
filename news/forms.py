from django.forms import ModelForm
from .models import Comment, Post
from allauth.account.forms import SignupForm
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


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user