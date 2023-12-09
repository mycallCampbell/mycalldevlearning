from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializer import BlogSerializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@api_view(['GET'])
def getBlogs(request):
    blogs = Blog.objects.filter(goLive='yes')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

def getBlog(request):
    blog = Blog.object.get(_id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

