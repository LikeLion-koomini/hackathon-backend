from rest_framework.generics import ListAPIView # 목록 조회를 편하게 해주는 모듈
from user.models import User # user/models에 있는 User 모델
from user.serializers import UserInfoSerializer # user/serializers에 있는 시리얼라이저

# user.models와 user.serializers의 __init__.py에서 필요한 모듈을 1차적으로 import함.

class UserListView(ListAPIView):
    # queryset : 키워드 속성이고, 데이터가 들어감
    queryset = User.objects.all()

    # serializer_class : 키워드 속성이고, 사용할 시리얼라이저가 들어감
    serializer_class = UserInfoSerializer

    # ListAPIView에서 제공하는 get 메서드의 오버라이드
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)