from django.db import models
from django.contrib.auth.models import User
from mongoengine import *


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    type1 = models.IntegerField(unique=True)
    type2 = models.IntegerField(unique=True)


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    regDate = models.DateTimeField(auto_now_add=True)
    modDate = models.DateTimeField(auto_now=True)


class Log(Document):
    name = StringField(required=True)
    value = DictField(required=True)
