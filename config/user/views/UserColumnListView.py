from column.models._init_ import Column
from rest_framework.generics import ListCreateAPIView
from column.serializers._init_ import ColumnSerializer

class UserColumnListView(ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    lookup_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)