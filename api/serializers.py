from rest_framework import serializers
from api import models


class Article(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.Article
        fields = ('user', 'username', 'title', 'content', 'modDate')