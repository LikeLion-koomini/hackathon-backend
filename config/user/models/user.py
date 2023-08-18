from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
import uuid

class UserManager(BaseUserManager):
    # 일반 사용자 생성
    def create_user(self, userId, password, **kwargs):
        user = self.model(userId=userId, **kwargs)
        user.set_password(password)
        user.save()

class User(AbstractBaseUser, PermissionsMixin):
    #AbstarctBaseUser는 user 커스텀할 때 사용
    #PermissionMixin는 장고의 기본 그룹, 허가권 관리 기능 재사용 가능
    class Meta:
      db_table = 'user'
      verbose_name = 'User'
      verbose_name_plural = 'Users'

    uuid = models.UUIDField(
        verbose_name="사용자 고유번호",
        primary_key=True,
        null=False,
        default=uuid.uuid4
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

    money = models.IntegerField(
        verbose_name='보유 금액',
        default=1000,
    )
    # User 모델의 필수 field
    # is_active = models.BooleanField(default=True)    
    # is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()
    USERNAME_FIELD = 'userId'