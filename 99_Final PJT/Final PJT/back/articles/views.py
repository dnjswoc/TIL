from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import MovieArticle, FreeArticle, MovieArticleComment, FreeArticleComment
from movies.models import Movie
from .serializers import MovieArticleListSerializer, FreeArticleListSerializer, MovieArticleSerializer, FreeArticleSerializer, MovieArticleCommentSerializer, FreeArticleCommentSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse



@api_view(['GET'])
def movie_article_list(request):
    # 영화 추천 게시판의 전체 게시글 목록을 조회
    if request.method == 'GET':
        movie_articles = MovieArticle.objects.all()
        serializer = MovieArticleListSerializer(movie_articles, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def free_article_list(request):
    # 자유게시판의 전체 게시글 목록을 조회
    if request.method == 'GET':
        free_articles = FreeArticle.objects.all().order_by('-created_at')
        serializer = FreeArticleListSerializer(free_articles, many=True)
        return Response(serializer.data)



@api_view(['GET', 'DELETE', 'PUT'])
def movie_article(request, movie_article_id, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    movie_article = MovieArticle.objects.get(id=movie_article_id)
    # 영화 추천 게시판의 단일 게시글 조회
    if request.method == 'GET':
        serializer = MovieArticleSerializer(movie_article)
        return Response(serializer.data)
    
    # 영화 추천 게시판의 단일 게시글 삭제
    elif request.method == 'DELETE':
        movie_article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 영화 추천 게시판의 단일 게시글 수정
    elif request.method == 'PUT':
        serializer = MovieArticleSerializer(movie_article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)
    




@api_view(['GET', 'DELETE', 'PUT'])
def free_article(request, free_article_id):
    free_article = FreeArticle.objects.get(id=free_article_id)
    # 자유게시판의 단일 게시글 조회
    if request.method == 'GET':
        serializer = FreeArticleSerializer(free_article)
        return Response(serializer.data)
    
    # 자유게시판의 단일 게시글 삭제
    elif request.method == 'DELETE':
        free_article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 자유게시판의 단일 게시글 수정
    elif request.method == 'PUT':
        serializer = FreeArticleSerializer(free_article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        



@api_view(['GET', 'POST'])
def movie_article_comment_list(request, movie_article_id):
    # 영화 추천 게시판에서 단일 게시글에 달린 댓글 전체 조회
    if request.method == 'GET':
        movie_article_comments = MovieArticleComment.objects.filter(article_id=movie_article_id)
        serializer = MovieArticleCommentSerializer(movie_article_comments, many=True)
        return Response(serializer.data)
    

    # 영화 추천 게시판에서 단일 게시글의 댓글 작성
    elif request.method == 'POST':
        movie_article = MovieArticle.objects.get(id=movie_article_id)
        serializer = MovieArticleCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=movie_article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'POST'])
def free_article_comment_list(request, free_article_id):
    # 자유게시판에서 단일 게시글에 달린 댓글 전체 조회
    if request.method == 'GET':
        free_article_comments = FreeArticleComment.objects.filter(article_id=free_article_id)
        serializer = FreeArticleCommentSerializer(free_article_comments, many=True)
        return Response(serializer.data)
    

    # 자유게시판에서 단일 게시글의 댓글 작성
    elif request.method == 'POST':
        free_article = FreeArticle.objects.get(id=free_article_id)
        serializer = FreeArticleCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=free_article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_article_comment(request, movie_id):
    # 영화 추천 게시판의 게시글 작성
    if request.method == 'POST':
        movie = Movie.objects.get(movie_id=movie_id)
        serializer = MovieArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def free_article_comment(request):
    # 자유게시판의 게시글 작성
    if request.method == 'POST':
        serializer = FreeArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def movie_article_comment_create(request, movie_article_id, comment_id):
    article = MovieArticle.objects.get(id=movie_article_id)
    comment = MovieArticleComment.objects.get(id=comment_id)

    # 영화 추천 게시판의 게시글에 작성된 댓글 조회
    if request.method == 'GET':
        serializer = MovieArticleCommentSerializer(comment)
        return Response(serializer.data)
    
    # 영화 추천 게시판의 게시글에 작성된 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 영화 추천 게시판의 게시글에 작성된 댓글 수정
    elif request.method == 'PUT':
        serializer = MovieArticleCommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data)
        



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def free_article_comment_create(request, free_article_id, comment_id):
    article = FreeArticle.objects.get(id=free_article_id)
    comment = FreeArticleComment.objects.get(id=comment_id)

    # 자유게시판의 게시글에 작성된 댓글 조회
    if request.method == 'GET':
        serializer = FreeArticleCommentSerializer(comment)
        return Response(serializer.data)
    
    # 자유게시판의 게시글에 작성된 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 자유게시판의 게시글에 작성된 댓글 수정
    elif request.method == 'PUT':
        serializer = FreeArticleCommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data)



@api_view(['POST'])
def movie_article_likes(request, movie_article_id):
    # 영화 추천 게시판의 게시글 좋아요 기능 구현
    if request.method == 'POST':
        article = MovieArticle.objects.get(id=movie_article_id)
        if request.user in article.like_users.all():
            article.like_users.remove(request.user)
            return JsonResponse({'message': '좋아요'})
        else:
            article.like_users.add(request.user)
            return JsonResponse({'message': '좋아요 취소'})



@api_view(['POST'])
def free_article_likes(request, free_article_id):
    # 자유게시판의 게시글 좋아요 기능 구현
    if request.method == 'POST':
        article = FreeArticle.objects.get(id=free_article_id)
        if request.user in article.like_users.all():
            article.like_users.remove(request.user)
            return JsonResponse({'message': '좋아요'})
        else:
            article.like_users.add(request.user)
            return JsonResponse({'message': '좋아요 취소'})
