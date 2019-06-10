from django.contrib.auth.models import User
from api.common import *


class Item(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    type1 = models.IntegerField(unique=True)
    type2 = models.IntegerField(unique=True)


class Test(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)


class Log(AbstractDynamicDocument):
    name = fields.StringField(required=True)
    value = fields.DictField(required=True)


class Comment(AbstractDynamicEmbeddedDocument):
    info = fields.DictField()
    content = fields.StringField(required=True)


class Article(AbstractDynamicDocument):
    info = fields.DictField()
    title = fields.StringField(required=True)
    content = fields.StringField(required=True)
    comments = fields.ListField(fields.EmbeddedDocumentField(Comment))
