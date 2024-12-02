# from rest_framework import serializers
# from dj_rest_auth.registration.serializers import RegisterSerializer
# from .models import User


# class CustomRegisterSerializer(RegisterSerializer):
#     # 필요한 필드들을 추가합니다.
#     nickname = serializers.CharField(
#     required=False,
#     allow_blank=True,
#     max_length=255
#     )

#     # 해당 필드도 저장 시 함께 사용하도록 설정합니다.
#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             # nickname 필드 추가
#             'nickname': self.validated_data.get('nickname', ''),
#         }

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie

# 회원가입 시 표기할 필드 지정
class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255
    )

    genre1 = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )

    genre2 = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )

    introduction = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )

    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname')
        user.genre1 = self.validated_data.get('genre1')
        user.genre2 = self.validated_data.get('genre2')
        user.introduction = self.validated_data.get('introduction')
        user.save()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname')
        data['genre1'] = self.validated_data.get('genre1')
        data['genre2'] = self.validated_data.get('genre2')
        data['introduction'] = self.validated_data.get('introduction')
        return data



from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


# 회원정보 수정
class CustomUserDetailsSerializer(UserDetailsSerializer):
    username = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    genre1 = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    genre2 = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    introduction = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'genre1', 'genre2', 'introduction')

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.genre1 = validated_data.get('genre1', instance.genre1)
        instance.genre2 = validated_data.get('genre2', instance.genre2)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.save()
        return instance





# 유저 정보 조회
class UserDetailSerializer(serializers.ModelSerializer):

    class UserFollowerSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',)


    class UserLikeMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'


    # 팔로잉, 팔로워 수를 필드로 추가
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)

    # 팔로워 목록
    followers = UserFollowerSerializer(many=True, read_only=True)

    # 좋아요 한 영화 목록 조회
    like_movies = UserLikeMovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
        # 유저가 작성한 댓글도 뽑을 수 있으면 추가해야함
        read_only_fields = ('followings', )