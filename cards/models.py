from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your tests here.
class UserCard(models.Model):
    title = models.CharField(max_length=20, blank=True)
    content = models.TextField(blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    userdeco = models.IntegerField(blank=True)
    chimneys = models.IntegerField(blank=True)


class Groupcard(models.Model):
    title = models.CharField(max_length=20, blank=True)
    content = models.TextField(blank=True)
    is_private = models.BooleanField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    groupdeco = models.IntegerField(blank=True)
    chimneys = models.IntegerField(blank=True)


class UserComment(models.Model):
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    usercard = models.ForeignKey(UserCard, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    socks = models.IntegerField(blank=True)
    id_text = models.TextField(blank=True)
    read = models.BooleanField(default=False)
    is_opened = models.BooleanField(default=False)


class Groupcomment(models.Model):
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    groupcard = models.ForeignKey(Groupcard, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    socks = models.IntegerField(blank=True)
    id_text = models.TextField(blank=True)
