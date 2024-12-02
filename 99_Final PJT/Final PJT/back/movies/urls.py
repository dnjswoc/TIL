from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 영화 목록 조회
    path('movies_list/', views.movies_list, name='movies_list'),

    # 장르별 영화 목록 조회
    path('movies_list/<str:genre_name>/', views.movies_list_genre, name='movies_list_genre'),

    # 단일 영화 조회
    path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    # 영화 좋아요 기능 구현
    path('<int:movie_id>/likes/', views.movie_likes, name='movie_likes'),

    # 영화 장르 목록 조회
    path('movie_genre_list/', views.movie_genre_list, name='movie_genre_list'),

    # 영화 한줄평(평점) 조회, 한줄평 생성
    path('movie_comment/<int:movie_id>/', views.movie_comments, name='movie_comment'),

    # 영화 한줄평(평점) 수정, 삭제
    path('movie_comment/<int:movie_id>/comment/<int:comment_id>/',
         views.movie_comment, name='movie_comment'),

    # 메인 페이지용 최신 영화 목록 조회
    path('latest_movie/', views.latest_movie, name='latest_movie'),
    
    # 영화 제목으로 영화 id 및 정보 조회
    # path('movie_detail/<str:movie_title>/', views.movie_detail, name='movie_detail'),

    # 챗봇 추천
    path('recommend_movies/<str:music_genre>/', views.recommend_movies, name='recommend_movies'),

    # assistant api
    path('recommend_movie/<str:music_genre>/', views.recommend_movie, name='recommend_movie'),
]