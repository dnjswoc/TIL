# 2024.10.04(금) PJT05 - 영화 프로젝트


#### `학습한 내용`

- 웹 크롤링이란?
  - 여러 웹 페이지를 돌아다니며 원하는 정보를 모으는 기술
  - 원하는 정보를 추출하는 스크래핑(Scraping)과 여러 웹 페이지를 자동으로 탐색하는 크롤링(Crawling)의 개념을 합쳐 웹 크롤링이라고 부름
  - 즉, 웹 사이트들을 돌아다니며 필요한 데이터를 추출하여 활용할 수 있도록 자동화된 프로세스

### 1. movies

#### `어려웠던 부분`

- 특히, update view함수에서 pk 인자 값을 가져와 어떤 식으로 context에 넘겨주면서 함수가 동작하는지 이 부분에서 헷갈렸던 부분이 있습니다.

```py
def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'movies/update.html',context)
```

- CSS는 여전히 어렵습니다ㅠㅠ

#### `새로 배운 것들`

- 백지 상태에서 앱 생성부터 model, view함수, templates를 하나하나 만들면서 어디 부분에서 막히는지를 제대로 알 수 있었습니다.

#### `느낀 점`

- 그 외에는 04pjt 부분에서 이미 구현해봤던 거여서 복습차원 겸 다시하게 되어 django 구현에 대해 확실하게 알게되었습니다.



### 2. accounts

#### `학습한 내용`

  - 저번 주에 배웠던 CRUD 내용에 더하여

#### `어려웠던 부분`

- 비밀번호 변경에서 PasswordChangeForm이 다른 폼들과 달라 구현하는 데 어려움이 있었습니다.

```py
@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

#### `새로 배운 것들`

- django form을 배우고 난 후 이번 주 들어와서 직접 만든 모델과 폼에서 그치지 않고, django에서 제공하는 built-in form, ModelForm을 사용하여 여러 기능을 구현했습니다.


#### `느낀 점`

- 이런 기능들을 사용하는 것에 익숙함을 느낄 수 있게 많은 노력과 연습이 필요한 것 같습니다.