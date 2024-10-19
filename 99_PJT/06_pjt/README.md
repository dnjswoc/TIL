# 06-pjt


## Movie 앱 담당 : 김나영

- movies 앱의 view함수 index, create, detail, update, delete 부분은 이제 자연스럽게 만들 수 있었습니다.
- 배운지 얼마 안된 likes부분이 어려워 역참조와 다시 원리에 대해서 공부가 필요한 것 같습니다.

```python
@login_required
def likes(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    if request.user in movie.like_users.all():   # 특히 이부분!!!
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')
```

#### CSS 부분에서 해결해야 할 점

- bootstrap 활용하여 카드를 col-6에 나타내는 부분이 어려웠었다..
- for문에서 카드를 생성하는 부분이 어려웠다는 점!

```python
<div class="container mt-3 mb-3">
  <div class="row">
    {% for movie in movies %}
      <div class="col-md-6 mb-4">
        <div class="card h-100">
          <h5 class="card-header">{{ movie.title }}</h5>
          <div class="card-body">
            <p class="card-text">
              <a href="{% url 'movies:detail' movie.pk %}" class="btn btn-link">DETAIL</a>
              {% if request.user in movie.like_users.all %}
              <a href="{% url "movies:likes" movie.pk %}"><button type="button" class="btn btn-outline-danger">좋아요 취소</button></a>
              {% else %}
              <a href="{% url "movies:likes" movie.pk %}"><button type="button" class="btn btn-outline-secondary">좋아요</button></a>
              {% endif %}
            </p>
          </div>
        </div>
      </div>
    {% empty %}
      <p>아직 등록된 영화가 없습니다.</p>
    {% endfor %}
  </div>
</div>
```



## Accounts 앱 담당 : 이원재

- auth 강의에서 진행한 login, logout, signup, update, delete, password change까지는 수월하게 진행할 수 있었습니다.
- 하지만 profile과 follow 부분에서 역참조 부분이 헷갈렸으며, movies 앱에서 진행한 좋아요까지 함께 생각하려니 코드 짜기 어려웠습니다.

```python
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

```html
{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <hr>
  <p>팔로워 : </p>
  <p>팔로잉 : </p>
  <hr>
  <h2>작성한 영화 목록</h2>
  <ul>
    {% for comment in person.comment_set.all %}
      <a href="{% url "movies:detail" comment.movie.pk %}">
        <li>{{ comment.movie }}</li>
      </a>
    {% empty %}
      <p>아직 작성한 영화가 없습니다.</p>
    {% endfor %}
  </ul>
  <hr>
  <h2>좋아요 누른 영화 목록</h2>
  <ul>
    {% for movie in person.like_movies.all %}
      <a href="{% url "movies:detail" movie.pk %}">
        <li>{{ movie.title }}</li>
      </a>
    {% empty %}
      <p>아직 좋아요를 누른 영화가 없습니다.</p>
    {% endfor %}
  </ul>
{% endblock content %}

```