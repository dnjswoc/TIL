from django.shortcuts import render

# Create your views here.
# view 함수의 첫 번째 인자가 항상 request인 이유?
# 그 view함수를 호출할 때, 첫번째 인자를 무조건 넣어주기 때문이다.
def hello(request):
    # template name -> template path
    # html 파일 이름 XXXXX -> html 파일 위치!
    return render(request, 'hello.html')