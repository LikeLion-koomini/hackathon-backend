from rest_framework.generics import RetrieveAPIView
from column.models import Column
from column.serializers import ColumnSerializer

class ColumnCertainView(RetrieveAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer