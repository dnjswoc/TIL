from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
     # 영화 추천 게시판 게시글 목록
     path('movie_article_list/', views.movie_article_list, name='movie_article_list'),

     # 자유게시판 게시글 목록
     path('free_article_list/', views.free_article_list, name='free_article_list'),

     # 영화 추천 게시판 게시글 작성
     path('movie_article/<int:movie_id>/comment/', views.movie_article_comment, name='movie_article'),
     
     # 자유게시판 게시글 작성
     path('free_article/comment/', views.free_article_comment, name='free_article_comment'),

     # 영화 추천 게시판 단일 게시글 조회, 삭제, 수정?
     path('movie_article/<int:movie_article_id>/<int:movie_id>/', views.movie_article, name='movie_article'),

     # 자유게시판 게시판 단일 게시글 조회, 삭제, 수정?
     path('free_article/<int:free_article_id>/', views.free_article, name='free_article'),

     # 영화 추천 게시판 게시글의 댓글 조회, 단일 댓글 생성
     path('movie_article/<int:movie_article_id>/comments/',
          views.movie_article_comment_list, name='movie_article_comment_list'),

     # 자유게시판 게시글의 댓글 목록 조회, 단일 댓글 생성
     path('free_article/<int:free_article_id>/comments/',
          views.free_article_comment_list, name='free_article_comment_list'),

     # 영화 추천 게시판 게시글 댓글 수정, 삭제
     path('movie_article/<int:movie_article_id>/comments/<int:comment_id>/',
          views.movie_article_comment_create,
          name='movie_article_comment_create'),

     # 자유게시판 게시글 댓글 수정, 삭제
     path('free_article/<int:free_article_id>/comments/<int:comment_id>/',
          views.free_article_comment_create,
          name='free_article_comment_create'),

     # 영화 추천 게시판 게시글 좋아요 기능 구현
     path('movie_article/<int:movie_article_id>/likes/',
          views.movie_article_likes,
          name='movies_article_likes'),

     # 자유게시판 게시글 좋아요 기능 구현
     path('free_article/<int:free_article_id>/likes/',
          views.free_article_likes,
          name='free_article_likes')
]