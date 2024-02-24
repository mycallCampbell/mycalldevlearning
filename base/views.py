from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Content
from .serializer import ContentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# BLOGS
@api_view(['GET'])
def getContent(request):
    contents = Content.objects.filter(goLive='yes')
    serializer = ContentSerializer(contents, many=True)
    return Response(serializer.data)



