from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Genre, Chart
from .serializers import MusicGenreSerializer, MusicChartSerializer
import requests
import base64



@api_view(['GET'])
# 노래 장르 목록 조회
def music_genre(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = MusicGenreSerializer(genres, many=True)
        return Response(serializer.data)
    



@api_view(['GET'])
# spotify 차트 불러오는 함수
def music_chart(request):
    if request.method == 'GET':
        musics = Chart.objects.all()[:10]
        serializer = MusicChartSerializer(musics, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def track_detail(request, track_id):
    if request.method == 'GET':
        # Spotify API 정보
        client_id = "71a6990fb99b4fca93e93c5109047c5d"  # Spotify Dashboard에서 복사
        client_secret = "b0fa375980864a3f8f2a720982ec7ed1"  # Spotify Dashboard에서 복사

        # Base64 인코딩
        auth_str = f"{client_id}:{client_secret}"
        auth_bytes = auth_str.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

        # 1. 토큰 요청
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {auth_base64}"
        }
        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.json()}")
            exit()

        # 토큰 추출
        token = response.json().get("access_token")
        print(f"Access Token: {token}")

        track_id = track_id

        api_url = f"https://api.spotify.com/v1/tracks/{track_id}"

        api_headers = {
            "Authorization": f"Bearer {token}"
        }

        api_response = requests.get(api_url, headers=api_headers)
        if api_response.status_code != 200:
            print(f"Error: {api_response.status_code}, {api_response.json()}")
            exit()

        data = api_response.json()
        return Response(data)