from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from api import models


class Item(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ('name', 'grade', 'type')


class Data(serializers.ModelSerializer):
    item = Item(many=True, read_only=True)

    class Meta:
        model = models.Data
        fields = ('item',)


class Log(DocumentSerializer):
    class Meta:
        model = models.Log
        read_only_fields = ('key', 'value')


class Article(DocumentSerializer):
    class Meta:
        model = models.Article
        fields = ('id', 'user', 'info', 'reg_date', 'mod_date', 'title', 'content')
        read_only_fields = ('id', 'reg_date', 'mod_date')


class Comment(DocumentSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'user', 'info', 'reg_date', 'mod_date', 'content')
        read_only_fields = ('id', 'reg_date', 'mod_date')
