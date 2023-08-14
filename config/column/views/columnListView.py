from rest_framework.generics import ListAPIView
from column.models import Column
from column.serializers import ColumnSerializer

class ColumnListView(ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer