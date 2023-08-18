# prod.py : 서버 환경을 담당
# 서버 환경에 맞게 고정 아이피를 등록하면 됨.

import os
from .base import *
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False

ALLOWED_HOSTS = ['your_domain', 'www.your_domain']
DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('SQL_DATABASE', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': env('SQL_USER', default='user'),
        'PASSWORD': env('SQL_PASSWORD', default='password'),
        'HOST': env('SQL_HOST', default='localhost'),
        'PORT': env('SQL_PORT', default=''),
    }
}

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True