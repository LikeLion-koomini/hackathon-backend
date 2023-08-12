from django.urls import path
from .views import UserListView

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view())
]