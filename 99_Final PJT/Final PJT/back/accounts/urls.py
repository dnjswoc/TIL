from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # 유저 프로필 조회
    path('profile/<int:user_id>/', views.profile, name='profile'),

    # follow 기능
    path('<int:user_id>/follow/', views.follow, name='follow'),

    # vue로 user_id 보내기
    path('get_user_id/', views.get_user_id, name='get_user_id'),
]