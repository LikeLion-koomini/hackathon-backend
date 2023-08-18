# local.py : 로컬 환경을 담당
# base.py의 모든 내용을 사용한다는 의미
# 따라서 local.py에서 base.py의 모든 내용을 사용할 수 있다.

import os
from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}