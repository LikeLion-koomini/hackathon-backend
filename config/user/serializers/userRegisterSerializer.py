from rest_framework import serializers
from user.models.user import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'userId', 'password', 'userName', 'email', 'phone_number', 'birth']

    def create(self, validated_data):
        uuid = validated_data.get('uuid')
        userId = validated_data.get('userId')
        password = validated_data.get('password')
        userName = validated_data.get('userName')
        email = validated_data.get('email')
        phone_number = validated_data.get('phone_number')
        birth = validated_data.get('birth')
        user = User(
            uuid = uuid,
            userId=userId, 
            userName=userName, 
            email=email, 
            phone_number=phone_number, 
            birth=birth
        )
        user.set_password(password)
        user.save()
        return user