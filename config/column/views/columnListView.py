from rest_framework.generics import ListAPIView
from column.models._init_ import Column
from column.serializers.columnSerializer import ColumnSerializer

class ColumnListView(ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)