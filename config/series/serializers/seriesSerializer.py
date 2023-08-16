from rest_framework import serializers
from series.models.series import Series
from user.serializers import UserInfoSerializer

class SeriesSerializer(serializers.ModelSerializer):
    writer = UserInfoSerializer
    columnCount = serializers.IntegerField(default=0)
    writerName = serializers.CharField(default=None)
    class Meta:
        model = Series
        fields = '__all__'
    
    def create(self, validated_data):
        # 시리즈 정보 추출
        series_id = validated_data.get('series_id')
        title = validated_data.get('title')
        content = validated_data.get('content')
        # 사용자 추출
        writer = self.context['request'].user
        writerName = writer.userName if writer.userName else None
        # 저장
        series = Series(
            series_id = series_id,
            title = title,
            content = content,
            writer = writer,
            writerName = writerName,
        )
        series.save()
        return series