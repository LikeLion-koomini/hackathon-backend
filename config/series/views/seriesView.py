from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from series.serializers import SeriesSerializer
from series.models.series import Series
from rest_framework import status
from rest_framework.response import Response

class SeriesListCreateView(ListCreateAPIView):
  queryset = Series.objects.all()
  serializer_class = SeriesSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, *kwargs)
  
  def post(self, request, *args, **kwargs):
    if not request.user:
      return Response({"message":"login first"}, status=status.HTTP_400_BAD_REQUEST)
    print(request.user.uuid)
    return self.create(request, *args, **kwargs)
  
  def perform_create(self, serializer):
    writer = self.request.user
    if writer: serializer.save(writer=writer)

class SeriesRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_url_kwarg = 'series_id'

    def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, *kwargs)