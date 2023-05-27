import requests
from django.dispatch import receiver
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Author, Category, PageMain, PageAbout, PageCourse, PageTeacher, PageContact, \
    BaseRegisterForm
from .filters import PostFilter
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_managers
from django.db.models.signals import post_save


@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.author} {instance.date_creation.strftime("%d %m %Y")}'
    else:
        subject = f'Appointment changed for {instance.author} {instance.date_creation.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.text,
    )

class Main(ListView):
    model = PageMain
    template_name = 'main.html'
    context_object_name = 'main'


class AboutUs(ListView):
    model = PageAbout
    template_name = 'about.html'
    context_object_name = 'about'


class Courses(ListView):
    model = PageCourse
    template_name = 'courses.html'
    context_object_name = 'courses'


class Teachers(ListView):
    model = PageTeacher
    template_name = 'tearchers.html'
    context_object_name = 'teachers'


class Contacts(ListView):
    model = PageContact
    template_name = 'contacts.html'
    context_object_name = 'contacts'

class PostList(ListView):
    model = Post
    template_name = 'blogs.html'
    context_object_name = 'blogs'
    queryset = Post.objects.order_by('-id')  # чтобы новость начиналась с последней добавленной
    paginate_by = 3  # постраничный вывод в один элемент

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='premium').exists()
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'blog'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

    # комменты
    def get_context_data(self, **kwargs):
        comment_list = super(PostDetail, self).get_context_data(**kwargs)
        comment_list['comments'] = Comment.objects.all()
        return comment_list


class PostAdd(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add.html'
    context_object_name = 'add'
    queryset = Post.objects.order_by()
    paginate_by = 10
    form_class = PostForm
    permission_required = ('news.add_post',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='premium').exists()
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        context['form'] = PostForm()
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'add.html'
    form_class = PostForm
    permission_required = ('news.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all
    success_url = '/blogs/'
    permission_required = ('news.delete_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')

