from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse


@api_view(['GET'])
def profile(request, user_id):
    if request.method == 'GET':
        User = get_user_model()
        person = User.objects.get(id=user_id)
        serializer = UserDetailSerializer(person)
        return Response(serializer.data)


@api_view(['POST'])
def follow(request, user_id):
    User = get_user_model()
    target_user = get_object_or_404(User, id = user_id)
    if request.method =='POST':
        if request.user == target_user:
            return JsonResponse({'error' :'자기 자신을 팔로우할 수 없습니다.'}, status = status.HTTP_400_BAD_REQUEST)
        if target_user in request.user.followings.all():
            request.user.followings.remove(target_user)
            return JsonResponse({'message': 'follow'})
        else:
            request.user.followings.add(target_user)
            return JsonResponse({'message': 'unfollow'})
        


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 로그인 한 유저의 정보를 vue에 전달하기 위한 함수
def get_user_id(request):
    serializer = UserDetailSerializer(request.user)
    return Response(serializer.data)