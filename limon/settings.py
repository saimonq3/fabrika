import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',

	'apps.main',
	'apps.planning',
]

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
	'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 2,
}

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES = (
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'limon.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
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

WSGI_APPLICATION = 'limon.wsgi.application'


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.getenv('DB_NAME'),
		'USER': os.getenv('DB_USER'),
		'PASSWORD': os.getenv('DB_PASSWORD'),
		'HOST': os.getenv('DB_HOST'),
		'PORT': os.getenv('DB_PORT'),
	}
}


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


CELERY_TASK_RESULT_EXPIRES = 3600
CELERY_TASK_DEFAULT_QUEUE = os.getenv("CELERY_DEFAULT_QUEUE")
CELERY_DEFAULT_QUEUE = os.getenv("CELERY_DEFAULT_QUEUE")
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = False
STATIC_URL = 'statica/'
STATIC_ROOT = 'statica/'
STATICFILES_DIRS = ['staticfiles/']

CSRF_TRUSTED_ORIGINS = [
	'https://fabrikainta.ru',
	'https://api.fabrikainta.ru',
	'http://api.fabrikainta.ru',
	'http://192.168.1.209:8800'
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
	'https://fabrikainta.ru',
	'https://api.fabrikainta.ru',
	'http://api.fabrikainta.ru',
	'http://192.168.1.209:8800'
]
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT']
CORS_ALLOW_HEADERS = [
	'accept',
	'accept-encoding',
	'authorization',
	'contenttype',
	'content-type',
	'dnt',
	'origin',
	'user-agent',
	'x-csrftoken',
	'x-requested-with',
	'token',
	'headers',
	'Access-Control-Allow-Origin',
	'strict-origin-when-cross-origin'
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = os.getenv('MEDIA_URL')

if not MEDIA_URL:
	MEDIA_URL = '/media/'


TIME_START = os.getenv('TIME_START')
TIME_STOP = os.getenv('TIME_STOP')

HOURS_WORK = [i for i in range(int(TIME_START), int(TIME_STOP) + 1)]
SYSTEM_NOTIFICATIONS_TELEGRAM_BOT_TOKEN = os.getenv('SYSTEM_NOTIFICATIONS_TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
