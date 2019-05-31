from datetime import datetime
from rest_framework_jwt.settings import api_settings


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
