# 2024년 11월 11일(월) 수업 내용 정리 - Vue Router


- Routing



- Vue Router

  - Basic Routing
  - Named Routes
  - Dynamic Route Matching
  - Nested Routes
  - Programmatic Navigation


- Navigation Guard

  - Globally Guard
  - Per-route Guard
  - In-component Guard


- 참고

  - Lazy Loading Routes



## Routing

- Routing

  - 네트워크에서 경로를 선택하는 프로세스
  
  - 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술


- SSR에서의 Routing

  ![alt text](./images/image_00.png)

  - SSR에서 routing은 서버 측에서 수행

  - 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송

  - 링크를 클릭하면 브라우저는 서버로부터 HTML 응답을 수신하고 새 HTML로 전체 페이지를 다시 로드


- CSR에서의 Routing

  ![alt text](./images/image_01.png)

  - CSR에서 routing은 **클라이언트 측**에서 수행

  - 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드 하지 않음


- SPA에서 Routing이 없다면

  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음

  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음

    - URL이 1개이기 때문에 새로 고침 시 처음 페이지로 되돌아감

    - 링크를 공유할 시 첫 페이지만 공유 가능

  - 브라우저의 뒤로 가기 기능을 사용할 수 없음

  - 페이지는 1개이지만, 주소에 따라 여러 컴포넌트를 새로 렌더링 하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 함




## Vue Router

- Vue Router

  - Vue 공식 라우터(The official Router for Vue.js)


- 사전 준비

  - Vite로 프로젝트 생성 시 Router 추가

    ![alt text](./images/image_02.png)

  - 서버 실행 후 Router로 인한 프로젝트 변화 확인

  - Home, Abaout 링크에 따라 변경되는 URL과 새로 렌더링 되는 화면

    ![alt text](./images/image_03.png)


- Vue 프로젝트 구조 변화

  1. App.vue 코드 변화

  2. router 폴더 신규 생성

  3. views 폴더 신규 생성

    ![alt text](./images/image_04.png)


- RouterLink

  - 페이지를 다시 로드하지 않고 URL을 변경하여 URL 생성 및 관련 로직을 처리

  - HTML의 \<a> 태그를 렌더링

    ![alt text](./images/image_05.png)


- RouterView

  - RouterLink URL에 해당하는 컴포넌트를 표시

  - 원하는 곳에 배치하여 컴포넌트를 레이아웃에 표시할 수 있음

    ![alt text](./images/image_06.png)



### Basic Routing

### Named Routes

### Dynamic Route Matching

### Nested Routes

### Programmatic Navigation


## Navigation Guard

### Globally Guard

### Per-route Guard

### In-component Guard


## 참고

### Lazy Loading Routes