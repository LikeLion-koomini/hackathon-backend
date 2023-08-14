from rest_framework.generics import RetrieveUpdateDestroyAPIView
from user.serializers.userInfoSerializer import UserInfoSerializer
from user.models.user import User

class UserCRUDView(RetrieveUpdateDestroyAPIView):
    # queryset : 사용할 데이터셋 설정
    queryset = User.objects.all()
    # serializer_class : 사용할 시리얼라이저 선택
    serializer_class = UserInfoSerializer
    # lookup_url_kwarg : 사용자를 구분할 기준 (여기서는 uuid) 제공
    lookup_url_kwarg = 'uuid'
        
    def get(self, request, *args, **kwargs): # 특정 사용자 정보 조회
        # bearer token으로 access_token 보내면 사용자 정보 조회 가능
        # if request.user:
        #     userdata = User.objects.get(userId=str(request.user))
        #     if userdata:
        #         serializer = UserInfoSerializer(userdata)
        #         print(serializer.data)
        return self.retrieve(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs): # 특정 사용자 정보 수정 ( 부분 수정 느낌 )
        return self.partial_update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs): # 특정 사용자 정보 제거 ( 사용자 삭제)
        return self.destroy(request, *args, **kwargs)