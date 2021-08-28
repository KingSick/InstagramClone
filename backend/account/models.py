from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)


class Follow(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    follow = models.ForeignKey(Member, on_delete=models.CASCADE)
