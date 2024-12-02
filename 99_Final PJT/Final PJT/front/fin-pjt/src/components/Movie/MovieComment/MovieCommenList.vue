<template>
   <!-- 한줄평 목록 -->
   <p>한줄평의 갯수 : <strong>{{ store.movieCommentsCount }}개</strong></p>
    <div v-if="store.movieCommentsCount === 0">
      <p>첫 한줄평을 작성해주세요!</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="comment in store.movieComments" :key="comment.id">
          <p>{{ comment }}</p>
          <p>한줄평 : {{ comment.content }}</p>

        </li>
      </ul>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
const store = useMovieStore()
const movieId = store.movieDetail.movie_id

onMounted(() => {
  store.getMovieComments(movieId)
})
</script>

<style scoped>

</style>