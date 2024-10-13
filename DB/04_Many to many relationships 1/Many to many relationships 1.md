# 2024년 10월 14일(월) 수업 내용 정리 - Many to many relationships 1


- Many to many relationships

  - N:1의 한계
  - 중개 모델
  - ManyToManyField
  - 'through' argument


- ManyToManyField



- 좋아요 기능 구현

  - 모델 관계 설정
  - 기능 구현




## Many to many relationships

- Many to many relationships(N:M or M:N)

  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

  - **양 쪽 모두에서 N:1 관계를 가짐**


- M:N 관계의 역할과 필요성 이해하기

      - '병원 진료 시스템 모델 관계'를 만들며 M:N 관계의 역할과 필요성 이해하기
      
      - 환자와 의사 2개의 모델을 사용하여 모델 구조 구상하기

      ⇨ 제공된 '99-mtn-practice' 프로젝트를 기반으로 진행



### N:1의 한계

- 의사와 환자 간 모델 관계 설정

  - 한 명의 의사에게 여러 환자가 예약할 수 있도록 설계

    ![alt text](./images/image_00.png)


- 의사와 환자 데이터 생성

  - 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약

    ![alt text](./images/image_01.png)


- N:1의 한계 상황

  - 1번 환자(carol)가 두 의사 모두에게 진료를 받고자 한다면 환자 테이블에 1번 환자 데이터가 중복으로 입력될 수 밖에 없음

    ![alt text](./images/image_02.png)

  - 동시에 예약을 남길 수는 없을까?

    ![alt text](./images/image_03.png)

      - 동일한 환자지만 다른 의사에게도 진료 받기 위해 예약하기 위해서는
        객체를 하나 더 만들어 진행해야 함

      - 외래 키 컬럼에 '1, 2' 형태로 저장하는 것은 DB 타입 문제로 불가능

      ⇨ "예약 테이블을 따로 만들자"



### 중개 모델

1. 예약 모델 생성

  - 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 생성

  - 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

    ![alt text](./images/image_04.png)


2. 예약 데이터 생성

  - 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행

  - 의사와 환자 생성 후 예약 만들기

    ![alt text](./images/image_05.png)


3. 예약 정보 조회

  - 의사와 환자가 예약 모델을 통해 각각 본인의 진료 내역 확인

    ![alt text](./images/image_06.png)


4. 추가 예약 생성

  - 1번 의사에게 새로운 환자 예약 생성

    ![alt text](./images/image_07.png)


5. 예약 정보 조회

  - 1번 의사의 예약 정보 조회

    ![alt text](./images/image_08.png)


#### Django에서는 'ManyToManyField'로 중개 모델을 자동으로 생성




### ManyToMany Field

- ManyToManyField()

  - M:N 관계 설정 모델 필드


- Django ManyToManyField

  - 환자 모델에 ManyToManyField 작성

    - 의사 모델에 작성해도 상관 없으며 참조/역참조 관계만 잘 기억할 것

    ![alt text](./images/image_09.png)

  - 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행

  - 생성된 중개 테이블 hospitals_patient_doctors 확인

    ![alt text](./images/image_10.png)

  - 의사 1명과 환자 2명 생성

    ![alt text](./images/image_11.png)

  - 예약 생성 (환자가 예약)

    ![alt text](./images/image_12.png)

  - 예약 생성 (의사가 예약)

    ![alt text](./images/image_13.png)

  - 중개 테이블에서 예약 현황 확인

    ![alt text](./images/image_14.png)

  - 예약 취소하기 (삭제)

  - 이전에는 Reservation을 찾아서 지워야 했다면, 이제는 .remove()로 삭제 가능

    ![alt text](./images/image_15.png)


#### 만약 예약 정보에 병의 증상, 예약일 등 추가 정보가 포함되어야 한다면?



### 'through' argument

- 'through' argument
  
  - 중개 테이블에 **'추가 데이터'**를 사용해 M:N 관계를 형성하려는 경우에 사용


- 'through' argument

  - Reservation Class 재작성 및 through 설정

    - 이제는 예약 정보에 "증상"과 "예약일"이라는 추가 데이터가 생김

      ![alt text](./images/image_16.png)
      

  - 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행

  - 의사 1명과 환자 2명 생성

    ![alt text](./images/image_17.png)

  - 예약 생성 방법 - 1

    - Reservation class를 통한 예약 생성

      ![alt text](./images/image_18.png)

  - 예약 생성 방법 - 2

    - Patient 또는 Doctor의 인스턴스를 통한 예약 생성 (**through_defaults**)

      ![alt text](./images/image_19.png)

  - 생성된 예약 확인

    ![alt text](./images/image_20.png)

  - 생성과 마찬가지로 의사와 환자 모두 각각 예약 삭제 가능

    ![alt text](./images/image_21.png)



- M:N 관계 주요 사항

      - M:N 관계로 맺어진 두 테이블에는 물리적인 변화가 없음

      - ManyToManyField는 중개 테이블을 자동으로 생성

      - ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음

        - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

      - N:1은 완전한 종속의 관계였지만 M:N은 종속적인 관계가 아니며
        '의사에게 진찰받는 환자 & 환자를 진찰하는 의사' 이렇게 2가지 형태 모두 표현 가능





## ManyToManyField

- ManyToManyField(to, **options)

 - M:N 관계 설정 시 사용하는 모델 필드


- ManyToManyField 특징

      - 양방향 관계

        - 어느 모델에서든 관련 객체에 접근할 수 있음

      - 중복 방지

       - 동일한 관계는 한 번만 저장됨



- ManyToManyField의 대표 인자 3가지

      1. related_name

      2. symmetrical

      3. through



1. 'related_name' arguments

  - 역참조 시 사용하는 manager naem을 변경

    ![alt text](./images/image_22.png)


2. 'symmetrical' arguments

  - 관계 설정 시 대칭 유무 설정

  - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용

  - 기본 값 : True

    ![alt text](./images/image_23.png)

  - True일 경우

    - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)

    - 즉, 내가 당신의 친구라면 자동으로 당신도 내 친구가 됨

  - False일 경우

    - True와 반대(대칭되지 않음)

      ![alt text](./images/image_24.png)


3. 'through' arguments

  - 사용하고자 하는 중개모델을 지정

  - 일반적으로 "추가 데이터를 M:N 관계와 연결하려는 경우"에 활용

    ![alt text](./images/image_25.png)



- M:N에서의 대표 조작 methods

  - add()

    - 관계 추가

    - "지정된 객체를 관련 객체 집합에 추가"

  - remove()

    - 관계 제거

    - "관련 객체 집합에서 지정된 모델 객체를 제거"

    


## 좋아요 기능 구현


### 모델 관계 설정

- Many to many relationships

  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

  - **양쪽 모두에서 N:1 관계를 가짐**


- Article(M) - User(N)

  - 0개 이상의 게시글은 0명 이상의 회원과 관련

  - 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있음


- 모델 관계 설정

  - Article 클래스에 ManyToManyField 작성

    ![alt text](./images/image_26.png)

  - Migration 진행 후 에러 발생

    ![alt text](./images/image_27.png)

  - related_name 작성 후 Migration 재진행

    ![alt text](./images/image_28.png)

  - 생성된 중개 테이블 확인

    ![alt text](./images/image_29.png)


- 역참조 매니저 충돌 1

      - N:1

        - "유저가 작성한 게시글"

        - user.article_set.all()

      - M:N

        - "유저가 좋아요 한 게시글"

        - user.article_set.all()


- 역참조 매니저 충돌 2

      - like_users 필드 생성 시 자동으로 역참조 매니저 .article_set가 생성됨

      - 그러나 이전 N:1(Article-User) 관계에서 이미 같은 이름의 매니저를 사용 중

        - user.article_set.all() → 해당 유저가 작성한 모든 게시글 조회

      - 'user가 작성한 글 (user.article_set)'과
        'user가 좋아요를 누른 글 (user.article_set)'을 구분할 수 없게 됨

      ⇨ user와 관계된 ForeignKey 혹은 ManyToManyField 둘 중 하나에 related_name 작성 필요



- User - Article 간 사용 가능한 전체 related manager

      - article.user

        - 게시글을 작성한 유저 - N:1

      - user.article_set

        - 유저가 작성한 게시글(역참조) - N:1

      - article.like_users

        - 게시글을 좋아요 한 유저 - M:N

      - user.like_articles

        - 유저가 좋아요 한 게시글(역참조) - M:N




### 기능 구현

- url 작성

  ![alt text](./images/image_30.png)

- view 함수 작성

  ![alt text](./images/image_31.png)

- index 템플릿에서 각 게시글에 좋아요 버튼 출력

  ![alt text](./images/image_32.png)

- 좋아요 버튼 출력 확인

  ![alt text](./images/image_33.png)

- 좋아요 버튼 클릭 후 테이블 확인

  ![alt text](./images/image_34.png)