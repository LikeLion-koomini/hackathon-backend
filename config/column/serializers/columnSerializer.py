from rest_framework import serializers
from column.models._init_ import Column, ColumnPrefer

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'

class ColumnPreferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnPrefer
        fields = '__all__'