from column.models._init_ import Column
from user.models.user import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserInfoSerializer
from column.serializers._init_ import ColumnSerializer

class UserColumnView(ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    lookup_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        column_id = self.kwargs['column_id']
        try:
            column_data = Column.objects.get(column_id=column_id)
            serializer.save(column_id=column_data.column_id)
        except:
            return Response({"message":"column not exist"}, status=status.HTTP_400_BAD_REQUEST)