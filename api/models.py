from django.contrib.auth.models import User
from api.common import *


class Item(AbstractModel):
    name = models.CharField(max_length=10)
    type1 = models.IntegerField(unique=True)
    type2 = models.IntegerField(unique=True)


class Test(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)


class TestTest(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)


class Log(AbstractDynamicDocument):
    name = fields.StringField(required=True)
    value = fields.DictField(required=True)


class Article(AbstractDynamicDocument):
    title = fields.StringField(required=True)
    content = fields.StringField(required=True)


class Comment(AbstractDynamicDocument):
    article = fields.ReferenceField('Article')
    content = fields.StringField(required=True)
