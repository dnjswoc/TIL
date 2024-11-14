<template>
  <div>
    <h2>Movie Detail</h2>
    <p>제목 : {{ result.title }}</p>
    <p>설멍 : {{ result.overview }}</p>
    <p>출시일 : {{ result.release_date }}</p>
    <p>평점 : {{ result.vote_average }}</p>
    <!-- <p>{{url + `${result.poster_path}`}}</p> -->
    <img :src="url + `${result.poster_path}`" alt="img">
  </div>
</template>

<script setup>
import { ref } from 'vue'

const url = ref('https://image.tmdb.org/t/p/w500/')

defineProps({
  result: Object
})

</script>

<style scoped>

</style>