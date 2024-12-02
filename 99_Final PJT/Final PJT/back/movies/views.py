from django.shortcuts import render
from django.db.models import Q
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, MovieGenre, Comment
from .serializers import MovieListSerializer, MovieSerializer, MovieAllSerializer, MovieGenreSerializer, MovieCommentListSerializer
from django.contrib.auth import get_user_model
from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
import random
import re
import json
import time


# 전체 영화 목록 조회
@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    


# 장르별 영화 목록 조회
@api_view(['GET'])
def movies_list_genre(request, genre_name):
    if request.method == 'GET':
        # filter로 장르 1, 2, 3에 원하는 장르 이름 설정
        # order_by('-vote_average')로 평점 내림차순
        # [:10]로 개수 10개 추출
        movies = Movie.objects.filter(Q(genre1=genre_name)|Q(genre2=genre_name)|Q(genre3=genre_name)).order_by('-vote_average')[:10]
        serializer = MovieAllSerializer(movies, many=True)
        return Response(serializer.data)



# 단일 영화 조회(Detail 페이지용)
@api_view(['GET'])
def movie_detail(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.get(movie_id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    


@api_view(['POST'])
# 영화 좋아요 기능 구현
def movie_likes(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(movie_id=movie_id)
        if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
            print(movie.like_users.all())
            return JsonResponse({'message': '좋아요 취소'})
        else:
            movie.like_users.add(request.user)
            print(movie.like_users.all())
            return JsonResponse({'message': '좋아요'})
        

@api_view(['GET'])
# 영화 장르 목록 조회
def movie_genre_list(request):
    if request.method == 'GET':
        genres = MovieGenre.objects.all()
        serializer = MovieGenreSerializer(genres, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def movie_comments(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    
    # 영화 한줄평 목록 조회
    if request.method == 'GET':
        # 영화에 대한 댓글들 가져오기
        comments = Comment.objects.filter(movie=movie).order_by('-created_at')
        
        # 직렬화
        serializer = MovieCommentListSerializer(comments, many=True)
        
        # 댓글과 함께 평균 평점, 사용자별 댓글 갯수, 평균 평점을 반환
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieCommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_comment(request, movie_id, comment_id):
    movie = Movie.objects.get(movie_id=movie_id)
    comment = Comment.objects.get(id=comment_id)
    # 영화 단일 한줄평 조회
    if request.method == 'GET':
        serializer = MovieCommentListSerializer(comment)
        return Response(serializer.data)


    # 영화 단일 한줄평 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    # 영화 단일 한줄평 수정
    elif request.method == 'PUT':
        serializer = MovieCommentListSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data)
        

@api_view(['GET'])
# 최신 영화 top 10 목록 조회
def latest_movie(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(release_date__gt='2024-05-01').order_by('-vote_average')[:10]
        serializer = MovieAllSerializer(movies, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def movie_detail(request, movie_title):
#     if request.method == 'GET':
#         movie = Movie.objects.get(title=movie_title)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)



load_dotenv()
API_KEY = os.environ.get('OPENAI_API_KEY')

# OpenAI API 키 설정 (실제 환경에서는 환경 변수 등을 사용하여 안전하게 관리해야 합니다)
openai.api_key = API_KEY

# 기존 함수들은 그대로 유지...

@api_view(['GET'])
def recommend_movies(request, music_genre):
    song_genre = music_genre

    if not song_genre:
        return JsonResponse({"message": "Please provide a song genre."}, status=400)

    try:
        # TMDB 장르 리스트 (한국어)
        tmdb_genres = [
            "액션", "모험", "애니메이션", "코미디", "범죄", 
            "다큐멘터리", "드라마", "가족", "판타지", "역사", 
            "공포", "음악", "미스터리", "로맨스", "SF", 
            "TV 영화", "스릴러", "전쟁", "서부"
        ]

        # OpenAI API 요청
        prompt = (
            f"Based on the song genre '{song_genre}', suggest a movie genre. "
            f"Please only use one of the following movie genres, written in Korean: {', '.join(tmdb_genres)}. "
            f"Respond with just the movie genre name."
            f"And please recommend a movie genre that matches the mood of the song genre"
            f"And please recommend a movie genre without 음악"
        )
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # GPT-4o-mini 모델 사용
            messages=[
                {"role": "system", "content": "You are a capable movie recommender."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )

        # 응답에서 영화 장르 추출
        movie_genre_kr = response.choices[0].message.content.strip()
        print("Extracted Genre (KR):", movie_genre_kr)

        # TMDB 장르에 포함되지 않는 경우 예외 처리
        if movie_genre_kr not in tmdb_genres:
            return JsonResponse({"message": "The movie genre is not valid or recognized."}, status=400)

        # SQLite3 DB에서 해당 장르의 영화 검색
        movies = Movie.objects.filter(
            Q(genre1__icontains=movie_genre_kr)
            # Q(genre2__icontains=movie_genre_kr) |
            # Q(genre3__icontains=movie_genre_kr)
        )

        if not movies.exists():
            return JsonResponse({"message": f"No movies found for genre: {movie_genre_kr}"})

        # 결과 반환
        movie_list = [{"title": movie.title, "description": movie.overview} for movie in movies]
        return JsonResponse({"movies": movie_list})

    except Exception as e:
        return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)
    





api_key = API_KEY

client = OpenAI(api_key=api_key)


# # 새로운 assistant를 만들 때
# assistant = client.beta.assistants.create(
#     name="Movie Recommender",  # 챗봇의 이름을 지정합니다.
#     # 챗봇의 역할을 설명합니다.
#     instructions="You are a capable movie recommender.  User gives you a music genre. You should recommend movies that are similar to the atmosphere of the music genre. You should recommend 1-2 movies(only title) that exists in the file I posted. Give some reasons why you recommend movies. Please answer in Korean.",
#     model="gpt-4o",  # 사용할 모델을 지정합니다.
# )

# ASSISTANT_ID = assistant.id

ASSISTANT_ID = 'asst_tLBQAXWhPY9IAeyjxbvnLcfS'

# 2-2. 스레드를 새롭게 생성합니다.
def create_new_thread():
    # 새로운 스레드를 생성합니다.
    thread = client.beta.threads.create()
    return thread


thread = create_new_thread()
# 새로운 스레드를 생성합니다.
# show_json(thread)
# 새롭게 생성한 스레드 ID를 저장합니다.
THREAD_ID = thread.id


# 반복문에서 대기하는 함수
def wait_on_run(run, thread_id):
    while run.status == "queued" or run.status == "in_progress":
        # 3-3. 실행 상태를 최신 정보로 업데이트합니다.
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


def submit_message(assistant_id, thread_id, user_message):
    # 3-1. 스레드에 종속된 메시지를 '추가' 합니다.
    client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=user_message
    )
    # 3-2. 스레드를 실행합니다.
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    return run


def get_response(thread_id):
    # 3-4. 스레드에 종속된 메시지를 '조회' 합니다.
    return client.beta.threads.messages.list(thread_id=thread_id)


def print_message(response):
    for res in response:
        if res.role == 'assistant':
            print(f"[{res.role.upper()}]\n{res.content[0].text.value}\n")
            return f'{res.content[0].text.value}'



def ask(assistant_id, thread_id, user_message):
    run = submit_message(
        assistant_id,
        thread_id,
        user_message,
    )
    # 실행이 완료될 때까지 대기합니다.
    run = wait_on_run(run, thread_id)
    msg = print_message(get_response(thread_id).data[-2:])
    return msg


def parse_recommendation_string(response):
    # 정규 표현식으로 제목, 이유, ID 추출
    movie_pattern = r"\d+\.\s([^\-]+)\s-\s(.*?)-\s(\d+)"
    
    recommendations = []
    matches = re.findall(movie_pattern, response, re.DOTALL)
    
    for match in matches:
        movie_title = match[0].strip()
        reason = match[1].strip()
        movie_id = match[2].strip()
        recommendations.append({
            'title': movie_title,
            'reason': reason,
            'movie_id': int(movie_id)  # ID를 정수로 변환
        })
    
    return recommendations


@api_view(['GET'])
def recommend_movie(request, music_genre):
    if request.method == 'GET':
        # 새로운 스레드 생성
        thread = create_new_thread()
        thread_id = thread.id  # 새로 생성된 스레드 ID 사용

        run = ask(ASSISTANT_ID, thread_id, music_genre)
        # print(type(run))
        parsed_json = parse_recommendation_string(run)
        print(parsed_json)
        return JsonResponse(parsed_json, safe=False)