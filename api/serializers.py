from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from api import models


class Test(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.Test
        fields = ('user', 'username', 'title', 'content', 'reg_date', 'mod_date')


class Log(DocumentSerializer):
    class Meta:
        model = models.Log
        read_only_fields = ('key', 'value')


class Comment(DocumentSerializer):
    class Meta:
        model = models.Comment
        fields = ('user_id', 'content', 'reg_date')
        read_only_fields = ('id', 'info', 'reg_date', 'mod_date')


class Article(DocumentSerializer):
    comments = Comment

    class Meta:
        model = models.Article
        fields = ('user_id', 'title', 'content', 'comments')
        read_only_fields = ('id', 'info', 'reg_date', 'mod_date')
