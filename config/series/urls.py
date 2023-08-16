from django.urls import path
from series.views.seriesView import *

app_name = 'series'

urlpatterns = [
    # post : 시리즈 생성
    path('create/', SeriesListCreateView.as_view()),
    # get : 시리즈 조회
    path('', SeriesListCreateView.as_view()),
    # get/<series_id> : 특정 시리즈 조회
    path('<uuid:series_id>/', SeriesRetrieveView.as_view()),
]