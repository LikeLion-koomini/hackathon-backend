from django.urls import path
from .views import UserListView, UserRegisterView

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view()),
    path('login/', UserRegisterView.as_view())
]