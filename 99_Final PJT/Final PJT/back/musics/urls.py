from django.urls import path
from . import views

app_name = 'musics'
urlpatterns = [
    # 노래 장르 목록 가져오기
    path('music_genre/', views.music_genre, name='music_genre'),

    # spotify 차트 목록 가져오기
    path('music_chart/', views.music_chart, name='music_chart'),

    # spotify 트랙 정보 가져오기
    path('track_detail/<str:track_id>/', views.track_detail, name='track_detail'),
]