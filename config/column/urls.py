from django.urls import path
from .views._init_ import *

app_name = 'column'

urlpatterns = [
    path('', ColumnListView.as_view(), name='column-list'),
    path('<uuid:column_id>/', ColumnCertainView.as_view(), name='column-detail'),
    path('register/', ColumnCRUDView.as_view(), name='column-register'), # 이거 자동으로 칼럼 현재 사용자한테 넣어줌
    path('<uuid:column_id>/likes/<uuid:uuid>/', CheckPreferView.as_view(), name='check-like'),
    path('<uuid:column_id>/likes/', PreferView.as_view(), name='like'),
    path('search/', ColumnSearchListView.as_view(), name='column-search'),
]