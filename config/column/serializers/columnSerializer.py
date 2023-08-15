from rest_framework import serializers, fields
from column.models._init_ import Column, ColumnPrefer
from categoryTuple import CATEGORY_CHOICES

class ColumnSerializer(serializers.ModelSerializer):
    category = fields.MultipleChoiceField(choices=CATEGORY_CHOICES)
    class Meta:
        model = Column
        fields = '__all__'

class ColumnPreferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnPrefer
        fields = '__all__'