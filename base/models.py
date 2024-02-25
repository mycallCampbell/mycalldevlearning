from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

# Create your models here.

class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goLive = models.CharField(max_length=200, null=True, blank=True)
    contentTitleFrontend = models.CharField(max_length=200, null=True, blank=True)
    contentTitleBackend = models.CharField(max_length=200, null=True, blank=True)
    imageThumbnail = models.CharField(max_length=200, null=True, blank=True)
    contentTag = models.CharField(max_length=200, null=True, blank=True)
    published = models.CharField(max_length=200, null=True, blank=True)
    minuteRead = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.contentTitleFrontend