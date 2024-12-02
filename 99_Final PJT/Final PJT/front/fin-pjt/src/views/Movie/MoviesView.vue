<template>
  <div>
    <MovieSearch />
  </div>
</template>

<script setup>
import MovieSearch from '@/components/Movie/MovieSearch.vue'
import { useMovieStore } from '@/stores/movie';
import { ref, onMounted } from 'vue';

const store = useMovieStore()


// 마운트 시 영화의 모든 장르를 담은 배열을 불러옴
onMounted(() => {
  store.getGenreList()
})

</script>

<style scoped>
div {
  background-color: #000;
  color: #fff; /* 텍스트 색상을 흰색으로 설정하여 가독성을 높임 */
  min-height: 100vh; /* 화면 전체를 채우도록 설정 */
  padding: 16px; /* 적당한 여백을 추가 */
}
</style>