from rest_framework import serializers
from .models import MovieArticle, FreeArticle, MovieArticleComment, FreeArticleComment
from django.contrib.auth import get_user_model


# 영화 추천 게시판 게시글 목록 조회 serializer
class MovieArticleListSerializer(serializers.ModelSerializer):

    class UserNicknameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = UserNicknameSerializer(read_only=True)

    class Meta:
        model = MovieArticle
        fields = '__all__'



# 자유게시판 게시글 목록 조회 serializer
class FreeArticleListSerializer(serializers.ModelSerializer):

    class UserNicknameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = UserNicknameSerializer(read_only=True)

    class Meta:
        model = FreeArticle
        fields = '__all__'



# 영화 추천 게시판 단일 게시글 관련 serializer
class MovieArticleSerializer(serializers.ModelSerializer):

    class UserNicknameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = UserNicknameSerializer(read_only=True)    

    class Meta:
        model = MovieArticle
        fields = '__all__'

        # read_only_fields
        read_only_fields = ('movie', 'like_users',)



# 자유게시판 단일 게시글 관련 serializer
class FreeArticleSerializer(serializers.ModelSerializer):

    class UserNicknameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('nickname', )

    nickname = UserNicknameSerializer(read_only=True)

    class Meta:
        model = FreeArticle
        fields = '__all__'

        # 읽기 전용 필드 설정
        read_only_fields = ('user', 'like_users',)



# 영화 추천 게시판 게시글의 댓글 목록 조회, 단일 댓글 생성
class MovieArticleCommentSerializer(serializers.ModelSerializer):

    class UserNicknameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = UserNicknameSerializer(read_only=True)
    
    class Meta:
        model = MovieArticleComment
        fields = '__all__'
        read_only_fields = ('article', )



# 자유게시판 게시글의 댓글 목록 조회, 단일 댓글 생성
class FreeArticleCommentSerializer(serializers.ModelSerializer):

    class UserNicknameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = UserNicknameSerializer(read_only=True)

    class Meta:
        model = FreeArticleComment
        fields = '__all__'
        read_only_fields = ('article', )


