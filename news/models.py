from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class PageMain(models.Model):
    pass

class PageAbout(models.Model):
    pass

class PageCourse(models.Model):
    pass

class PageTeacher(models.Model):
    pass

class PageContact(models.Model):
    pass

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rat = self.post_set.all().aggregate(post_rating=Sum('rating'))
        p_rat = 0
        p_rat += post_rat.get('post_rating')

        comment_rat = self.user.comment_set.all().aggregate(comment_rating=Sum('rating'))
        c_rat = 0
        c_rat += comment_rat.get('comment_rating')

        self.rating_author = p_rat * 3 + c_rat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    date_creation = models.DateTimeField(auto_now_add=True)
    post = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=256)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    img = models.ImageField(blank=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:153] + '...'

    def get_absolute_url(self):
        return f'/blogs/'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    comm_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comm_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    def save(self):
        user = super(UserCreationForm, self).save()
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )