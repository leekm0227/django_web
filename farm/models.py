from django.contrib.auth.models import User
from farm.core import *


class Grade(AbstractModel):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)


class Type(AbstractModel):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)


class Item(AbstractModel):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


class Craft(AbstractModel):
    output = models.ForeignKey(Item, on_delete=models.CASCADE)
    input = models.ManyToManyField(Item, related_name='input')


class Account(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inventory = models.ManyToManyField(Item, through='Inventory')


class Inventory(AbstractModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item')
    amount = models.BigIntegerField(default=0)

    class Meta:
        unique_together = ('account', 'item')


# ======================================== MONGODB MODEL ===============================================================
class Log(AbstractDynamicDocument):
    name = fields.StringField(required=True)
    value = fields.DictField(required=True)


class Article(AbstractDynamicDocument):
    title = fields.StringField(required=True)
    content = fields.StringField(required=True)


class Comment(AbstractDynamicDocument):
    article = fields.ReferenceField('Article')
    content = fields.StringField(required=True)
