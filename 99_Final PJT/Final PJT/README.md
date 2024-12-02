# Final Project 

---
- 백 서버키기 전 준비사항

```bash
$ python manage.py migrate
$ python manage.py loaddata freearticle_dummy.json freearticlecomment_dummy.json movie_dummy.json moviearticle_dummy.json moviearticlecomment_dummy.json moviecomment_dummy.json moviegenre_dummy.json musicgenre_dummy.json user_dummy.json
$ python manage.py loaddata freearticle_dummy.json freearticlecomment_dummy.json  movie_dummy.json movie_prac1.json movie_prac2.json movie_prac3.json  moviearticle_dummy.json moviearticlecomment_dummy.json moviecomment_dummy.json moviegenre_dummy.json musicgenre_dummy.json  user_dummy.json

# movie_dummy.json 데이터로 다시 통합
$ python manage.py loaddata freearticle_dummy.json freearticlecomment_dummy.json movie_dummy.json moviearticle_dummy.json moviearticlecomment_dummy.json moviecomment_dummy.json moviegenre_dummy.json musicgenre_dummy.json user_dummy.json

# 24.11.26 기준
$ python manage.py loaddata chart.json freearticle_dummy.json freearticlecomment_dummy.json movie.json moviearticle_dummy.json moviearticlecomment_dummy.json moviecomment_dummy.json moviegenre_dummy.json musicgenre_dummy.json user_dummy.json

# 24.11.26 오후 기준(moviearticle 관련 json 파일 삭제)
$ python manage.py loaddata chart.json freearticle_dummy.json freearticlecomment_dummy.json movie.json moviecomment_dummy.json moviegenre_dummy.json musicgenre_dummy.json user_dummy.json

# 24.11.27 마지막 fixtures
$ python manage.py loaddata article.json articlecomment.json chart.json comment.json genre.json likes.json movie.json user.json

```



🎆 Daily 개발일지
---

### 24.11.18(월)

- 사이트 전체 구조 디테일 잡기

- [Front]
  - 기본 Navbar 구성

- [Back] 
  - User 모델 커스텀
  - Article, Movie Serializer 진행

#### Issue

- dj-rest-auth를 통해 User 모델을 커스텀하여 필드를 추가하고, 회원가입을 진행하던 중 email 필드에 Integrity Error가 계속 나타나 여러 방법을 강구

  - accounts의 serializers를 수정하여 회원가입 시 입력할 수 있는 필드를 추가하고,

  - dj-rest-auth 의 회원가입 정보는 all-auth 의 DefaultAccountAdapter 에서 DB에 저장되므로, 회원가입 시 추가 필드를 DB에 저장하고 싶다면DefaultAccountAdapter 를 상속받은 CustomAdapter를 만들어줘야한다.

    ```python
    from allauth.account.adapter import DefaultAccountAdapter

    class CustomAccountAdapter(DefaultAccountAdapter):
        def save_user(self, request, user, form, commit=True):
            user = super().save_user(request, user, form, commit=False)
            data = form.cleaned_data
            user.birth = data.get('nickname')
            if commit:
                user.save()
            return user
    ```

  - adapters 수정 후 settings.py에 수정된 adapters 추가

    ```python
    # adapter 세팅 추가
    ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'
    ```


- 현재 적용하려는 Open API 활용하여 챗봇 만들기 구글링 중 제대로 된 정보가 없지만 관련 서적 도움받아 해결하고자 함. 프롬프트가 중요해보임!!

```python
from openai import OpenAI
from pprint import pprint

# openAPI에서 발급받은 api_key적용
api_key = '발급받은 api_key'
client = OpenAi(api_key=api_key)

model = "적용할 Open API 모델"

messages = [
  # system은 언어모델의 페르소나를 설정하는 역할
  {"role" : "system", "content" : "~~~(페르소나 지정)"},
  {"role" : "user", "content" : "~~~(사용자의 질문 사항)"}
]

# 2가지 방법 존재
response = client.chat.completions.create(model=model, messages=meaages).model_dump()

propmt = """
내일 다음 주제로 미래 교육 포럼에서 발표할 발제문을 작성해야 합니다. 발제문의 주요 내용을 불릿 기호로 간략히 정리해 주세요.
주제 : {agenda}
""".format(agenda="인공지능 시대의 교육의 역할과 의미")

response = client.completions.create(
  modle = "사용 모델",
  messages = [{
    "role" : "user",
    "content" : prompt
  }]
)
```


### 24.11.19(화)

- 프론트 기본 틀 잡기(홈, 커뮤니티, 로그인, 회원가입)
- 조건 추가하여 장르별 영화 목록 추출, user정보 vue에 연결

- [Front]
  - main view Top10 영화 목록 보여주기(css까지 완성) - 영화 디테일 연결 아직 안함.
  - 커뮤니티 게시판 라우터 구성
  - signup, login css 기본 완성

- [Back] 
  - TMDB에서 가져온 영화 데이터를 영화 장르별로 보여주기 위해 django orm(filter, order_by)을 통해 추출
  - 장르별로 추출하고 TMDB 평점을 내림차순으로 정렬하여 그 중 일정 개수만 vue에 연결

#### Issue

- vue에서 데이터를 처리하려고 했는데 그것보다 django orm을 통해 미리 데이터를 처리하고 vue에 연결하는 것이 더 낫다고 판단

- django orm은 연결이 가능해 filter, order_by를 연결하여 데이터 추출



### 24.11.20.(수)

- 커뮤니티(자유게시판 CRUD 기능 구현 완성, 게시판 댓글 CR까지 구현 완료!)
- 프로필 페이지(유저 간 follow기능(본인에게 뜨지 않도록 구현하진 못했음), 로그아웃 및 회원정보 수정 기능 생성(프론트에서는 구현 못함))

- [Front] 

  - Back이랑 연결해서 커뮤니티 게시판 작성시 db저장 성공
  - 기본 CRUD 완성 / 댓글 생성, 읽기 + 카운트(computed쓸려했는데 복잡해져서 일단 보류) 까진 가능

- [Back]

  - 프로필 페이지에 user의 정보 연결하기 성공
  - 프로필 페이지에 user들 간 follow 기능 추가(follow, unfollow 버튼 토글까지 구현, 하지만 다른 사람의 프로필 페이지에서만 뜨도록 구현하지는 못함)
  - 로그아웃, 회원정보 수정 기능 구현(로그아웃 시 token값이 사라지지 않아 axios 요청 성공 후 직접 제거... 회원정보 수정은 postman에서만 시험, 프론트에서는 점검하진 못함)



#### Issue

- [Front] : 컴포넌트를 나눠서 파일 관리하려다보니 props를 쓰는게 복잡해지고 댓글 실시간 반영이 잘 안됐다. 그래서 댓글 폼 작성하는 곳에서 댓글 조회하는 목록을 다시 업로드 하는 로직을 구현!

```js
  // 댓글 목록을 다시 가져오는 함수
const fetchComments = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/free_article/${route.params.free_article_id}/comments/`,
  })
  .then((response) => {
    comments.value = response.data; // 댓글 목록 갱신
  })
  .catch((error) => {
    console.log(error);
  });
};

// 페이지 로드 시 댓글 목록 가져오기
fetchComments();


```

- [Back] : 회원정보 수정 기능은 dj-rest-auth 라이브러리를 이용하였는데 회원 가입과 비슷하게 기본 serializer로는 username, email 등 기본 필드만 수정 가능하여 UserDetailsSerializer를 커스터마이징하여 수정할 수 있는 필드 추가

```py
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

```


### 24.11.21.(목)

- 커뮤니티(자유게시판 CRUD, 각 게시판안에서 댓글 CRUD 최종 구현 완료!!!!!)
- + 작성자와 수정,삭제하려는 사람이 같아야만 수정,삭제 기능 가능하도록 구현도 완료!!!
- 로그아웃, 회원정보 수정 기능 다듬기(jwt 방식의 로그아웃 포기, 회원정보 수정 기능 프로트에서 구현해보기, 회원정보 수정 링크로 이동 시 기존에 저장된 유저 정보가 뜨도록 수정 필요), 로그인 한 유저의 정보(id 뿐만 아니라 모든 정보) 프론트에 연결
- 영화 검색 페이지 채우기(장르별 인기 영화 목록 나열 및 왼쪽, 오른쪽 화살표 클릭 시 포스터 포커스 이동)


#### Issue

- [Front] 
  - 댓글 안에서 CR까지 됐는데 컴포넌트 여러개로 쪼개고 prop, emit 방식쓰다보니 머리 터져버렸..
  - 6시간 헤매다가 큰맘먹고 파일 다 밀고 pinia로 다시 접근,, 바로 클린코드 되어버림.. 바보짓한 내탓이오...내탓이오.. 그래도 반응형 잘되고 뿌-듯!!
  - 까먹었던 computed 바로 써먹어버리기 여러곳에서 활용가능하니 기억하기!!!

```js
  // 자유게시판 댓글 갯수 세기
  const freeArticleCommentCount = computed(() => {
    return comments.value.length
  })
```

- [Back]

  - jwt 방식으로 dj-rest-auth를 바꾸니 로그아웃 시 로그인 후 발급 받은 토큰은 깔끔하게 없어졌지만 로그인 시 기존에 발급 받던 토큰이 아닌 access token과 refresh token으로 발급 받아 이를 로그인에 사용하는 법을 찾지 못해 jwt 방식을 포기 후 vue에서 로그아웃 시 token을 제거하는 방식으로 수정
  - 장르별 영화 목록을 불러오기 위해 장르 목록을 반복하며 pinia에 저장된 함수를 불러다 onMounted 썼는데 마지막에 저장된 장르 영화 목록만 장르 개수만큼 반복하였음... pinia에 저장된 영화 목록이 반응형이라 마지막에 저장된 것을 반복한다는 것을 깨닫고 장르는 반복하되 장르별 영화 목록은 컴포넌트에서 직접 함수를 작성하여 문제를 해결

  ```js
  <template>
    <div>
      <h3>{{ genre.name }}</h3>
      <div class="carousel-container">
      <button class="arrow left" @click="scrollLeft">‹</button>
      <div class="carousel" v-if="movieGenreList">
        <MovieGenrePopularList 
        v-for="(movie, index) in visibleMovies"
          :key="index"
          :movie="movie"
        />
      </div>
      <button class="arrow right" @click="scrollRight">›</button>
    </div>
    </div>
    
  </template>

  <script setup>
  import { ref, onMounted, computed } from 'vue';
  import { useMovieStore } from '@/stores/movie';
  import { useAccountStore } from '@/stores/account';
  import MovieGenrePopularList from './MovieGenrePopularList.vue';
  import axios from 'axios';

  const movieGenreList = ref(null)
  const currentIndex = ref(0) // 현재 시작 포스터의 인덱스

  const store = useMovieStore()
  const accountStore = useAccountStore()
  const API_URL = store.API_URL
  const token = accountStore.token

  const props = defineProps({
    genre: Object
  })

  const visibleMovies = computed(() => {
    if (movieGenreList.value.length === 0) return []
    const moviesCount = movieGenreList.value.length
    return Array.from({ length: 10 }, (_, i) => movieGenreList.value[(currentIndex.value + i) % moviesCount])
  })

  const scrollLeft = () => {
    const moviesCount = movieGenreList.value.length
    currentIndex.value = (currentIndex.value - 1 + moviesCount) % moviesCount // 왼쪽으로 이동 시 인덱스 조정
  }

  const scrollRight = () => {
    const moviesCount = movieGenreList.value.length
    currentIndex.value = (currentIndex.value + 1) % moviesCount // 오른쪽으로 이동 시 인덱스 조정
  }


  onMounted(() => {
    axios({
      method : 'get',
      url : `http://127.0.0.1:8000/movies/movies_list/${props.genre.name}/`,
      headers : {
        Authorization : `Token ${token}`
      }
    })
      .then((res) => {
        console.log(res.data)
        movieGenreList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  })

  </script>

  <style scoped>

  </style>
  ```


  
### 24.11.22.(금)

- ㅇㅇ
- 회원정보 수정 시 기존 정보가 나타나도록 수정, 비밀번호 변경 기능 추가
- 챗봇 기능 테스트



#### Issue

- [Front]

  - ㅇㅇ

- [Back]

  - 처음 회원정보 수정 시 빈 값으로 수정을 하기 때문에 사용자가 빈 값을 그대로 두고 수정할 값만 수정한 채로 form을 작성하면 빈 값이 그대로 저장되어 불편함을 느낄 수 있으므로 기존에 저장된 사용자의 정보를 가져와 미리 form을 채워 넣어 사용자 편의를 제고

  ```js
  // 기존 회원정보를 기반으로 수정할 수 있게 값을 저장해놓고 시작
  
  const nickname = ref(userId.nickname)
  const genre1 = ref(userId.genre1)
  const genre2 = ref(userId.genre2)
  const introduction = ref(userId.introduction)
  ```






### 24.11.23.(토)

- ㅇㅇ
- 영화 한줄평을 남기기 위한 url, view, serializer 생성(한줄평을 남긴 유저 정보를 나타내기 위한 serializer 수정), fixtures 수정
- openai api를 이용한 챗봇 만들기 계속 시도


#### Issue

- [Front]

  - ㅇㅇ

- [Back]

  - 기존에 만들었던 챗봇은 사용자가 좋아하는 노래 장르를 입력하면 그와 어울리는 영화 장르를 대답해 주고 답변 받은 영화 장르 기반으로 우리가 가지고 있는 DB의 영화 데이터에서 일치하는 장르를 가진 영화를 추출하는 방식을 고려했다. 하지만 이 방식의 단점은 영화의 장르는 한정적이고, 영화 장르보다 노래 장르가 더 다양하므로 챗봇의 답변 결과가 단조롭다는 것이다. 그래서 openai api를 더 알아보니 assistant를 통해 직접 파일을 업로드하면 업로드한 파일에서 답변을 해주는 기능을 찾았다. 내일 이것에 대해서 더 알아보고 다시 만들어봐야겠다...





### 24.11.24.(일)

- ㅇㅇ
- 노래 장르 목록 조회를 위한 url, view, serializer 생성(spotify api 사용), fixtures(genre_dummy.json) 수정
- openai api를 이용한 assistant api 생성 계속 계속 시도...(그래도 많이 나아지는 중), assistant api 프론트에 연결(디테일 페이지, 유튜브 예고편까지)

#### Issue

- [Front]

  - ㅇㅇ

- [Back]

  - openai api의 assistant 기능을 한참 공부하고, 여기저기 알아본 후 openai의 playground에서 만들어보니 어제 만들었던 챗봇보다는 답변이 더 다양하게 나오고 쓸 만 해진 것 같다. 코드가 너무 길어 여기에 작성하기는 힘들 것 같다. 그리고 assistant의 답변이 일정한 것 같다가도 한 번씩 달라져 JsonResponse로 넘겨줄 데이터가 아예 달라져서 프롬프트를 더 꼼꼼하게 작성했다. 프롬프트의 중요성을 다시 한번 깨달았다.





### 24.11.25.(월)

- ㅇㅇ
- musics app에 Music 모델 추가 및 spotify 이번 주 인기 차트 데이터 등록, spotify 데이터 프론트에 연결(앨범 이미지, 디테일 페이지, youtube api로 뮤직비디오 연결)
- 영화 데이터 fixtures 수정(설명이 부실한 영화 데이터를 제외) 및 메인 페이지 영화 목록 수정(TMDB에서 바로 가져오지 않고 DB의 영화 데이터에서 가져오도록 수정)


#### Issue

- [Front] 

  - ㅇㅇ

- [Back]

  - ㅇㅇ