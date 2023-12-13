from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goLive = models.CharField(max_length=200, null=True, blank=True)
    blogTitle = models.CharField(max_length=200, null=True, blank=True)
    imageThumbnail = models.CharField(max_length=200, null=True, blank=True)
    imageHeroMobile = models.CharField(max_length=200, null=True, blank=True)
    imageHeroDesktop = models.CharField(max_length=200, null=True, blank=True)
    imageWidthMobile = models.IntegerField(null=True, blank=True, default=0)
    imageHeightMobile = models.IntegerField(null=True, blank=True, default=0)
    imageWidthDesktop = models.IntegerField(null=True, blank=True, default=0)
    imageHeightDesktop = models.IntegerField(null=True, blank=True, default=0)
    imageRef1 = models.CharField(max_length=200, null=True, blank=True)
    imageRef2 = models.CharField(max_length=200, null=True, blank=True)
    imageRef3 = models.CharField(max_length=200, null=True, blank=True)
    minuteRead = models.IntegerField(null=True, blank=True, default=0)
    tagTeaser = models.CharField(max_length=200, null=True, blank=True)
    tagCompletion = models.CharField(max_length=200, null=True, blank=True)
    subTitle1 = models.CharField(max_length=200, null=True, blank=True)
    subTitle2 = models.CharField(max_length=200, null=True, blank=True)
    subTitle3 = models.CharField(max_length=200, null=True, blank=True)
    subTitle4 = models.CharField(max_length=200, null=True, blank=True)
    caption1 = models.CharField(max_length=200, null=True, blank=True)
    caption2 = models.CharField(max_length=200, null=True, blank=True)
    captchaPhrase = models.TextField(null=True, blank=True)
    callToAction1 = models.TextField(null=True, blank=True)
    callToAction2 = models.TextField(null=True, blank=True)
    callToAction3 = models.TextField(null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    description4 = models.TextField(null=True, blank=True)
    description5 = models.TextField(null=True, blank=True)
    description6 = models.TextField(null=True, blank=True)
    description7 = models.TextField(null=True, blank=True)
    description8 = models.TextField(null=True, blank=True)
    description9 = models.TextField(null=True, blank=True)
    description10 = models.TextField(null=True, blank=True)
    description11 = models.TextField(null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.blogTitle


class Podcast(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goLive = models.CharField(max_length=200, null=True, blank=True)
    podcastTitle = models.CharField(max_length=200, null=True, blank=True)
    imageThumbnail = models.CharField(max_length=200, null=True, blank=True)
    imageHeroMobile = models.CharField(max_length=200, null=True, blank=True)
    imageHeroDesktop = models.CharField(max_length=200, null=True, blank=True)
    imageWidthMobile = models.IntegerField(null=True, blank=True, default=0)
    imageHeightMobile = models.IntegerField(null=True, blank=True, default=0)
    imageWidthDesktop = models.IntegerField(null=True, blank=True, default=0)
    imageHeightDesktop = models.IntegerField(null=True, blank=True, default=0)
    imageRef1 = models.CharField(max_length=200, null=True, blank=True)
    imageRef2 = models.CharField(max_length=200, null=True, blank=True)
    imageRef3 = models.CharField(max_length=200, null=True, blank=True)
    minuteRead = models.IntegerField(null=True, blank=True, default=0)
    tagTeaser = models.CharField(max_length=200, null=True, blank=True)
    tagCompletion = models.CharField(max_length=200, null=True, blank=True)
    subTitle1 = models.CharField(max_length=200, null=True, blank=True)
    subTitle2 = models.CharField(max_length=200, null=True, blank=True)
    caption1 = models.CharField(max_length=200, null=True, blank=True)
    caption2 = models.CharField(max_length=200, null=True, blank=True)
    captchaPhrase = models.TextField(null=True, blank=True)
    callToAction1 = models.TextField(null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.podcastTitle