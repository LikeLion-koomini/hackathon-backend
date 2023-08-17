from rest_framework import serializers
from column.models._init_ import Column
from user.serializers.userInfoSerializer import UserInfoSerializer

class ColumnRegisterSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    class Meta:
        model=Column
        field= "__all__"
    
    def create(self, validated_data):
        column_id = validated_data.get('column_id')
        title = validated_data.get('title')
        content = validated_data.get('content')
        created_at = validated_data.get('created_at')
        prefer = validated_data.get('prefer')
        category = validated_data.get('category')
        price = validated_data.get('price')
        column = Column(
            column_id=column_id,
            title=title,
            content=content,
            created_at=created_at,
            prefer=prefer,
            category=category,
            price=price,
        )
        column.save()
        return column