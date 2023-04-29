from django.urls import path, include
from .views import PostList, PostDetail, PostAdd, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView

urlpatterns = [
    path('', PostList.as_view(), name='blogs'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add', PostAdd.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name = 'sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name = 'sign/signup.html'), name='signup'),


]