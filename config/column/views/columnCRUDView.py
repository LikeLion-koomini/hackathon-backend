from rest_framework.generics import ListCreateAPIView
from column.models.column import Column
from user.models.user import User
from column.serializers.columnSerializer import ColumnSerializer
from column.serializers.columnRegisterSerializer import ColumnRegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class ColumnCRUDView(ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    # 필요한 정보 ( 여기서는 현재 사용자의 칼럼 목록) 을 반환
    # 나중에 수정 / 삭제 시 ListCreateAPIView 내부에서 사용함

    def get_queryset(self): # 
        user_uuid = self.request.user.uuid
        queryset = Column.objects.filter(user=user_uuid)
        return queryset
    
    # ListCreateAPIView의 메서드 오버로딩
    # post > create에서 현재 로그인한 user 데이터를 저장 
    # ( 현재 사용자 인증은 bearer 토큰으로 access token을 넘겨주면 자동으로 해줌 )
    def perform_create(self, serializer):
        user = self.request.user
        if user: serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        if not request.user:
            return Response(
                {"message":"need to login"}
                ,status=status.HTTP_400_BAD_REQUEST
            )
        return self.create(request, *args, **kwargs)
              
