from rest_framework import fields, serializers
from user.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    # model : 사용할 모델
    # fields : 보여줄 데이터들
    class Meta:
        model = User
        fields = '__all__'