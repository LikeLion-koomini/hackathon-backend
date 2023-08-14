from django.urls import path
from column.views import ColumnListView, ColumnCertainView, CheckPreferView, PreferView

app_name = 'column'

urlpatterns = [
    path('column/', ColumnListView.as_view(), name='column-list'),
    path('column/<int:pk>/', ColumnCertainView.as_view(), name='column-detail'),
    path('column/<int:column_id>/likes/<int:user_id>/', CheckPreferView.as_view(), name='check-like'),
    path('column/<int:column_id>/likes/<int:user_id>/', PreferView.as_view(), name='like'),
]