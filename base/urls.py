from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.getContent, name='getContent'),
]