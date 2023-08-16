from rest_framework.generics import ListAPIView
from column.models._init_ import Column
from column.serializers.columnSerializer import ColumnSerializer
from django.db.models import Q

class ColumnSearchListView(ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def get_queryset(self):
        # 검색 데이터 추출
        title = self.request.data.get("title")
        category = self.request.data.get("category")
        uuid = self.request.data.get('uuid')
        # 쿼리셋 추출
        queryset = Column.objects.none()
        if title is not None: 
            queryset = Column.objects.filter(Q(title__contains=title))
        if category is not None:
            for item in category:
                queryset = queryset | Column.objects.filter(Q(category__contains=item) | Q(category__contains=[item]))
        if uuid is not None:
                queryset = queryset | Column.objects.filter(user=uuid)
        # 데이터 반환
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)