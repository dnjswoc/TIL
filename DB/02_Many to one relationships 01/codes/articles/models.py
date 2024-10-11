from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # user = models.ForeignKey(유저, 유저가 탈퇴했을때 이 유저가 작성한 게시글을 어떻게 처리할지)   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # article = models.ForeignKey(상대 모델 클래스, 상대 모델 클래스가 삭제되었을 때 댓글을 어떻게 처리할지)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

