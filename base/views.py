from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog, Podcast
from .serializer import BlogSerializer, PodcastSerializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# BLOGS
@api_view(['GET'])
def getBlogs(request):
    blogs = Blog.objects.filter(goLive='yes')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBlog(request, pk):
    blog = Blog.objects.get(_id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

# PODCAST
@api_view(['GET'])
def getPodcasts(request):
    podcasts = Podcast.objects.filter(goLive='yes')
    serializer = PodcastSerializer(podcasts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPodcast(request, pk):
    podcast = Podcast.objects.get(_id=pk)
    serializer = PodcastSerializer(podcast, many=False)
    return Response(serializer.data)

