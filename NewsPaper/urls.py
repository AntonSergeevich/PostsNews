from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import Main, AboutUs, Courses, Teachers, Contacts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='main'),
    path('about/', AboutUs.as_view(), name='about'),
    path('courses/', Courses.as_view(), name='courses'),
    path('teachers/', Teachers.as_view(), name='teachers'),
    path('contact/', Contacts.as_view(), name='contacts'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('blogs/', include('news.urls')),
    path('accounts/', include('allauth.urls')),
    path('reviews/', include('reviews.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
