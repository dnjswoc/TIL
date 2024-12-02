from rest_framework import serializers
from .models import Movie, Comment, MovieGenre
from django.contrib.auth import get_user_model


# 영화 목록 조회
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'vote_average', 'poster_path', )



# 영화 목록 모든 필드 조회(장르별 조회 및 디테일 페이지용)
class MovieAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



# 단일 영화 조회
class MovieSerializer(serializers.ModelSerializer):

    # 역참조 관계인 comment 가져오기
    class MovieCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('content', 'score', )

    comment_set = MovieCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


# 영화 장르 목록
class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = '__all__'


# 영화 한줄평 목록 조회
class MovieCommentListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', )