from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, userId, password, **kwargs):
        user = self.model(userId=userId, **kwargs)
        user.set_password(password)
        user.save()

class User(AbstractBaseUser):
    class Meta:
      db_table = 'user'
      verbose_name = 'User'
      verbose_name_plural = 'Users'

    uuid = models.UUIDField(
        verbose_name='사용자 고유번호',
        primary_key=True,
        null=False,
    )

    userId = models.CharField(
        verbose_name='사용자 아이디',
        max_length=100,
        null=False,
        unique=True,
    )

    password = models.CharField(
        verbose_name='사용자 비밀번호',
        max_length=100,
        null=False,
    )

    userName = models.CharField(
        verbose_name='사용자 이름',
        max_length=100,
        null=False,
    )

    email = models.CharField(
        verbose_name='사용자 이메일',
        max_length=100,
        null=False,
    )

    phone_number = models.CharField(
        verbose_name='사용자 전화번호',
        max_length=30,
        null=False,
        unique=True,
    )

    birth = models.DateField(
        verbose_name='사용자 생년월일',
        null=False,
    )