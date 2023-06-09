from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import Main, AboutUs, Courses, Teachers, Contacts, PostList
from django.views.decorators.cache import cache_page



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(60*1)(Main.as_view()), name='main'),
    path('about/', AboutUs.as_view(), name='about'),
    path('courses/', Courses.as_view(), name='courses'),
    path('teachers/', Teachers.as_view(), name='teachers'),
    path('contact/', Contacts.as_view(), name='contacts'),
    path('blogs/', PostList.as_view(), name='blogs'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('/', include('news.urls')),
    path('accounts/', include('allauth.urls')),
    path('reviews/', include('reviews.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
