from rest_framework.generics import RetrieveUpdateDestroyAPIView
from column.models.column import Column
from column.serializers.columnSerializer import ColumnSerializer

class ColumnCertainView(RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    # lookup 필드 생성 --> 이걸로 칼럼들 서로 구분함. 
    # (urls.py에서 칼럼 id를 column_id로 설정했기 때문에 lookup_field를 column_id로 해야함)
    lookup_field = 'column_id'

    # 현재 view에 대한 get 명령이 없어서 추가함.
    def get(self, request, *args, **kwargs): # 특정 칼럼 정보 조회
        return self.retrieve(request, *args, **kwargs)