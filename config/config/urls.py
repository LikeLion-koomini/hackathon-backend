from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

routers = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="프로젝트 이름(예: humanscape-project)",
        default_version='프로젝트 버전(예: 1.1.1)',
        description="해당 문서 설명(예: humanscape-project API 문서)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="이메일"), # 부가정보
        license=openapi.License(name="mit"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # swagger 세팅
    re_path(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # 실제 사용하는 URL
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('column/', include('column.urls')),
    path('series/', include('series.urls'))
]