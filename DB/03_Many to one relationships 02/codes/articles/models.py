# articles/models.py
from django.db import models
from django.conf import settings

# Article (N) : User (1)
class Article(models.Model):
    # user에 대한 정보 외래키로 설정
    # 일반적인 다른 app으로부터 Model을 import 받아왔을때 발생하는 문제
    # settings.py -> INSTALLED_APPS에 등록한 순서에 영향을 받는다.
    # 코드 실행 순서에 대한 엄청난 복잡한 이야기가 있엇다.
    # 근데.. 그 복잡한거 뭔지 모르겠고, 아무튼 잘 돌아가게 하려면
    # 선언된적 없는 객체를 할당하는게 아니라, 그냥 문자열을 할당한다.
        # 근데... 개발자는 똑같은거 여러번쓰는거 진짜 싫어함.
    # 현재 활성화 된 User 모델이 무엇인지는 settings.py에 이미 써놧었다.
        # AUTH_USER_MODEL = 'accounts.User' 라는 모델을 문자열로 적어둠.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # on_delete 왜하는걸까요?
    # CASCADE -> 내 참조 대상이 DB에서 사라졌을때, 나도 함께 삭제.
    # 지금은 django로 연습 중 -> 항상 CASCADE -> 제일 안귀찮음.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
