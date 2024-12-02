<template>
  <div class="menu">
    <!-- <RouterLink :to="{name : 'movie_article'}">영화 게시판</RouterLink> | 
    <RouterLink :to="{name : 'free_article'}">자유 게시판</RouterLink> -->
  </div>
    <RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue';
import { useCommunityStore } from '@/stores/community';

const store = useCommunityStore()

onMounted(() => {
  store.getfreeArticles()
  store.getMovieArticles()
})

</script>

<style scoped>

.menu {
  text-align: center; /* 메뉴를 가운데 정렬 */
  margin-top: 80px; /* 상단 여백 추가 */
}

.menu a {
  text-decoration: none; /* 밑줄 제거 */
  color: #444; /* 기본 텍스트 색상 */
  font-weight: bold; /* 텍스트 굵게 */
  font-size: 1.2rem; /* 글자 크기 */
  padding: 10px 15px; /* 내부 여백 */
  transition: color 0.3s ease, background-color 0.3s ease; /* 호버 효과를 부드럽게 */
  border: 2px solid transparent; /* 테두리 기본값 */
  border-radius: 5px; /* 둥근 모서리 */
}

.menu a:hover {
  color: #fff; /* 호버 시 텍스트 색상 */
  background-color: forestgreen; /* 호버 시 배경색 */
  border-color: forestgreen; /* 테두리도 색상 변경 */
}

.menu a.router-link-exact-active {
  color: #fff; /* 활성화 상태의 텍스트 색상 */
  background-color: darkgreen; /* 활성화 상태의 배경색 */
  border-color: darkgreen; /* 활성화 상태의 테두리 색상 */
}
</style>
