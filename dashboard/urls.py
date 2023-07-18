from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),
#blog gen routes
    path('generate-blog-topic', views.blogTopic, name='blog-topic'),
    path('generate-blog-sections', views.blogSections, name='blog-sections'),
    
]

