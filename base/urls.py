from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.getBlogs, name='getBlogs'),
    path('guides/', views.getPodcasts, name='getGuides'),
]