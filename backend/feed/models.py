from django.db import models
from account.models import Member


class Feed(models.Model):
    author = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)


class HashTag(models.Model):
    tag = models.CharField(max_length=255)
    feed = models.ForeignKey(to=Feed, on_delete=models.CASCADE)
