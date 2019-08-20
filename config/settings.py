import os
import socket
import datetime
import mongoengine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'h9lb28wfcxyxt)bt!l2ep-4(b4_!9#bv&(x0-nb^7s-62_qvx#'

USE_I18N = True
USE_L10N = True
USE_TZ = True
DEBUG = True
APPEND_SLASH = True
SITE_ID = 1
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
STATIC_URL = '/static/'
WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'
API_URL = "http://127.0.0.1:8000/api/"
ALLOWED_HOSTS = []

# db settings
DB_NAME = 'django'
DB_USER = 'django'
DB_PASSWORD = '1234'
DB_HOST = '35.239.104.137'
DB_PORT = '3306'
DB_OPTION = {
    'sql_mode': 'TRADITIONAL',
    'charset': 'utf8',
    'init_command': "SET storage_engine=INNODB, "
                    "character_set_connection=utf8, "
                    "collation_connection=utf8_general_ci, "
                    "sql_mode='STRICT_TRANS_TABLES'"
}

# allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "none"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'id'
EMAIL_HOST_PASSWORD = 'pwd'
REST_USE_JWT = False
REST_SESSION_LOGIN = False
REST_AUTH_TOKEN_CREATOR = 'api.common.create_token'

INSTALLED_APPS = [
    'api',
    'web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'rest_framework_mongoengine',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'OPTION': DB_OPTION,
    }
}

mongoengine.connect('django', host='35.239.104.137', port=27017)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_AUTH_SERIALIZERS = {
}

JWT_AUTH = {
    'JWT_PAYLOAD_HANDLER': 'api.common.jwt_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'api.common.jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

if 'instance' in socket.gethostname():
    API_URL = "https://thell.ga/api"
    ALLOWED_HOSTS = ['*']
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTION': DB_OPTION,
        }
    }
