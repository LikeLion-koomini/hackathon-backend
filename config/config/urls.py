from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

routers = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('column/', include('column.urls')),
]