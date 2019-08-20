from django.contrib.auth.models import User
from api.common import *


class Grade(AbstractModel):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Type(AbstractModel):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(AbstractModel):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')

    def __str__(self):
        return self.name


class Craft(AbstractModel):
    output = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='output')
    input = models.ManyToManyField(Item, related_name='input')


class Data(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    inventory = models.ManyToManyField(Item, through='Inventory')


class Inventory(AbstractModel):
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='data')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item', )
    amount = models.BigIntegerField(default=0)

    class Meta:
        unique_together = ('data', 'item')


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
