from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from api import models


class Article(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.Article
        fields = ('user', 'username', 'title', 'content', 'modDate')


class Log(DocumentSerializer):
    class Meta:
        model = models.Log
        fields = ('name', 'value')
