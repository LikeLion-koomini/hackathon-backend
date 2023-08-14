from user.models.user import User
from rest_framework import serializers

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'userId', 'userName',]