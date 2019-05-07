from datetime import datetime
from rest_framework_jwt.settings import api_settings


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
        'test': 'test'
    }
