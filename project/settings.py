import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': f'{os.getenv("DB_HOST")}',
        'PORT': f'{os.getenv("DB_PORT")}',
        'NAME': f'{os.getenv("DB_NAME")}',
        'USER': f'{os.getenv("DB_USER")}',
        'PASSWORD': f'{os.getenv("DB_PASSWORD")}'
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = eval(f'{os.getenv("DEBUG").lower().capitalize()}')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
