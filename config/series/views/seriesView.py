from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from series.serializers import SeriesSerializer
from series.models.series import Series
from user.models.user import User
from column.models.column import Column
from rest_framework import status
from rest_framework.response import Response

class SeriesListCreateView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
  queryset = Series.objects.all()
  serializer_class = SeriesSerializer
  
  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())

    page = self.paginate_queryset(queryset)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    for instance in queryset:
      # 칼럼 갯수 저장
      columnCountQuerySet = Column.objects.filter(series_id=instance.series_id)
      if columnCountQuerySet.exists: columnCount = columnCountQuerySet.count()  # QuerySet의 개수를 가져옴
      else: columnCount=0
      instance.columnCount = columnCount
      # 인스턴스 저장
      instance.save()
      
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, *kwargs)
  
  def post(self, request, *args, **kwargs):
    if not request.user:
      return Response({"message":"login first"}, status=status.HTTP_400_BAD_REQUEST)
    return self.create(request, *args, **kwargs)

  def perform_create(self, serializer):
    # 사용자 uuid 저장
    writer = self.request.user
    if writer:
       serializer.save(writer=writer)

class SeriesRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_url_kwarg = 'series_id'

    def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      # 시리즈 내부 칼럼 갯수
      columnCountQuerySet = Column.objects.filter(series_id=serializer.data.get('series_id'))
      columnCount = columnCountQuerySet.count()  # QuerySet의 개수를 가져옴
      # 데이터 저장
      serializer_data = serializer.data
      serializer_data['columnCount'] = columnCount
      # 응답
      return Response(serializer.data)

    def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, *kwargs)