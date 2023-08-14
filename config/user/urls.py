from django.urls import path
from .views import UserListView, UserRegisterView,UserLoginView,UserCRUDView

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view()),
    path('signup/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()), #post
    path('logout/', UserLoginView.as_view()), #delete
    path('<uuid:uuid>/', UserCRUDView.as_view()), #get
]