from django.db import models
from datetime import datetime

from django.forms.models import model_to_dict
from mongoengine import (DynamicDocument, fields)
from rest_framework_jwt.settings import api_settings

META = {
    'allow_inheritance': True,
    'abstract': True,
    'index_cls': False,
    # 'index_opts': {},
    # 'index_background': True,
    # 'auto_create_index': True,
}


def create_token(token_model, user, serializer):
    token_model.objects.filter(user=user).delete()
    token, _ = token_model.objects.get_or_create(user=user)
    return token


def jwt_payload_handler(user):
    return {
        'user_id': user.pk,
        'username': user.username,
        'email': user.email,
        'exp': datetime.now() + api_settings.JWT_EXPIRATION_DELTA,
    }


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': {
            'username': user.username,
            'email': user.email,
        }
    }


class AbstractModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(model_to_dict(self))

    class Meta:
        abstract = True


class AbstractDynamicDocument(DynamicDocument):
    id = fields.SequenceField(primary_key=True)
    user = fields.DictField(required=True)
    info = fields.DictField(null=True)
    reg_date = fields.DateTimeField(default=datetime.now())
    mod_date = fields.DateTimeField(default=datetime.now())
    is_delete = fields.BooleanField(default=False)
    meta = META

    def save(self, *args, **kwargs):
        self.mod_date = datetime.now()
        return super(AbstractDynamicDocument, self).save(*args, **kwargs)
