from rest_framework import fields, serializers
from user.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'userId', 'userName','email', 'phone_number', 'birth']