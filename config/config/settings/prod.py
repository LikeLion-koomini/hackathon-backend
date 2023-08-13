# prod.py : 서버 환경을 담당
# 서버 환경에 맞게 고정 아이피를 등록하면 됨.

from .base import *
DEBUG=True
ALLOWED_HOSTS = ['3.37.58.70']