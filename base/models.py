from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goLive = models.CharField(max_length=200, null=True, blank=True)
    blogTitleFrontend = models.CharField(max_length=200, null=True, blank=True)
    blogTitleBackend = models.CharField(max_length=200, null=True, blank=True)
    imageThumbnail = models.CharField(max_length=200, null=True, blank=True)
    imageHeroMobile = models.CharField(max_length=200, null=True, blank=True)
    minuteRead = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.blogTitleFrontend


class Guide(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goLive = models.CharField(max_length=200, null=True, blank=True)
    podcastTitle = models.CharField(max_length=200, null=True, blank=True)
    imageThumbnail = models.CharField(max_length=200, null=True, blank=True)
    imageHeroMobile = models.CharField(max_length=200, null=True, blank=True)
    minuteRead = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.podcastTitle