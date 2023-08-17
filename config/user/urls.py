from django.urls import path
from .views import UserListView, UserRegisterView,UserLoginView,UserCRUDView,UserColumnListView, UserColumnView

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view()),
    path('signup/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()), #post
    path('logout/', UserLoginView.as_view()), #delete
    path('<uuid:uuid>/', UserCRUDView.as_view()), #get : 특정 사용자의 정보 조회
    path('<uuid:uuid>/column/', UserColumnListView.as_view()), # get : 특정 사용자가 작성한 칼럼 목록 조회
    path('<uuid:uuid>/column/<uuid:column_id>/', UserColumnView.as_view()), # get : 특정 사용자가 작성한 특정 칼럼 조회
]