from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from api import models


class Test(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.Test
        fields = ('id', 'user', 'username', 'title', 'content', 'reg_date', 'mod_date')


class TestTest(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.TestTest
        fields = ('id', 'user', 'username', 'content', 'reg_date', 'mod_date')


class Log(DocumentSerializer):
    class Meta:
        model = models.Log
        read_only_fields = ('key', 'value')


class Article(DocumentSerializer):
    class Meta:
        model = models.Article
        fields = ('id', 'user', 'reg_date', 'mod_date', 'title', 'content')
        read_only_fields = ('id', 'reg_date', 'mod_date')


class Comment(DocumentSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'user', 'reg_date', 'mod_date', 'content')
        read_only_fields = ('id', 'reg_date', 'mod_date')
