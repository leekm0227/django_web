from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    type1 = models.IntegerField(unique=True)
    type2 = models.IntegerField(unique=True)


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    regDate = models.DateTimeField(auto_now_add=True)
    modDate = models.DateTimeField(auto_now=True)