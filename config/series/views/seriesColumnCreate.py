from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from series.serializers import SeriesSerializer
from column.serializers.columnSerializer import ColumnSerializer
from series.models.series import Series
from user.models.user import User
from column.models.column import Column
from rest_framework import status
from rest_framework.response import Response

class SeriesColumnCreate(ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    lookup_url_kwarg = 'series_id'

    def perform_create(self, serializer):
        user = self.request.user
        series = Series.objects.get(series_id=self.kwargs['series_id'])
        if user: serializer.save(user=user, series_id=series)
      
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)