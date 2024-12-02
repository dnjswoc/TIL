<template>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
  </head>
  <nav class="header">
    <div>
      <RouterLink :to="{ name: 'home' }" class="advanced-logo" @click="scrollToTop">
        <span class="headphones-icon">
          <i class="fas fa-headphones"></i>
        </span>
        BMW
      </RouterLink>
    </div>
    <div class="nav-menu">
      <!-- 로그인 안된 경우 -->
      <div v-if="!store.token">
        <RouterLink :to="{ name: 'home' }" @click="scrollToTop" :class="{ active: isActive('home') }">홈</RouterLink>
        <RouterLink :to="{ name: 'movies' }" @click="scrollToTop" :class="{ active: isActive('movies') }">영화</RouterLink>
        <RouterLink :to="{ name: 'free_article' }" @click="scrollToTop" :class="{ active: isActive('free_article') }">커뮤니티</RouterLink>
        <RouterLink :to="{ name: 'login' }" @click="scrollToTop" :class="{ active: isActive('login') }">로그인</RouterLink>
        <RouterLink :to="{ name: 'signup' }" @click="scrollToTop" :class="{ active: isActive('signup') }">회원가입</RouterLink>
      </div>

      <!-- 로그인 된 경우 -->
      <div v-else>
        <RouterLink :to="{ name: 'home' }" @click="scrollToTop" :class="{ active: isActive('home') }">홈</RouterLink>
        <RouterLink :to="{ name: 'movies' }" @click="scrollToTop" :class="{ active: isActive('movies') }">영화</RouterLink>
        <RouterLink :to="{ name: 'free_article' }" @click="scrollToTop" :class="{ active: isActive('free_article') }">커뮤니티</RouterLink>
        <RouterLink :to="{ name: 'profile' }" @click="scrollToTop" :class="{ active: isActive('profile') }">My Page</RouterLink>
        <a @click="logOut">로그아웃</a>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink, useRoute } from 'vue-router'
import { useAccountStore } from '@/stores/account'
import { onMounted } from 'vue'

const store = useAccountStore()

const route = useRoute()

const logOut = function () {
  store.logOut()
}


// 페이지 상단으로 스크롤
const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth', // 부드럽게 스크롤
  });
};

// 현재 페이지 경로와 매칭 확인
const isActive = (name) => route.name === name;
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

/* 헤더 스타일 */

/* 현재 활성화된 페이지에 대한 스타일 */
.nav-menu a.active {
  user-select: none;
  color: #FFD700; /* 활성화된 링크 텍스트 색상 */
  background-color: rgba(255, 255, 255, 0.2); /* 활성화된 링크 배경색 */
  font-weight: bold; /* 텍스트 굵게 */
  border-radius: 5px; /* 둥근 모서리 */
}

main {
  margin-top: 60px; /* navbar 높이만큼 여백 추가 */
}

.header {
  height: 60px; /* 고정 높이 지정 */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px; /* 상하 15px, 좌우 30px */
  background-color: rgba(0, 0, 0, 0.9); /* 더 어두운 배경색으로 변경 */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); /* 그림자 약간 더 진하게 */
}

/* 로고 스타일 */
.advanced-logo {
  font-family: 'Arial', sans-serif;
  font-size: 2em; /* 적당한 크기로 줄임 */
  font-weight: bold;
  text-transform: uppercase;
  background: linear-gradient(45deg, #FF6347, #00BFFF);
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  gap: 10px;
  transition: transform 0.3s ease, text-shadow 0.3s ease;
}

/* 로고 hover 효과 */
.advanced-logo:hover {
  transform: scale(1.1); /* 로고 크기를 약간 키움 */
  text-shadow: 2px 2px 15px rgba(255, 99, 71, 0.8), 2px 2px 15px rgba(0, 191, 255, 0.8);
}

/* 아이콘 크기 및 색상 조정 */
.headphones-icon i {
  font-size: 1.2em;
  background: linear-gradient(45deg, #FF6347, #00BFFF); /* 로고와 같은 색상 그라데이션 */
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
}

/* 메뉴 스타일 */
/* 로그아웃 버튼 스타일 */
.nav-menu a {
  user-select: none;
  text-decoration: none;
  color: #ffffff;
  font-size: 1.1rem;
  font-family: 'Arial', sans-serif;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 5px;
  transition: all 0.3s ease-in-out;
  cursor: pointer; /* 기본적으로 커서를 손가락 모양으로 설정 */
}

.nav-menu a:hover {
  color: #FFD700;
  background-color: rgba(255, 255, 255, 0.1);
}

.nav-menu a:last-child { /* 로그아웃 버튼에만 스타일 적용 */
  cursor: pointer; /* 커서를 손가락 모양으로 변경 */
}

/* 반응형 레이아웃 */
@media (max-width: 768px) {
  .header {
    flex-wrap: wrap;
    padding: 10px 20px;
  }

  .nav-menu {
    flex-direction: column;
    gap: 10px;
    align-items: flex-end; /* 우측 정렬 */
  }

  .advanced-logo {
    margin-bottom: 10px;
  }
}

</style>

<style>
.main-content {
  margin-top: 60px; /* navbar 높이만큼 여백 추가 */
}
</style>