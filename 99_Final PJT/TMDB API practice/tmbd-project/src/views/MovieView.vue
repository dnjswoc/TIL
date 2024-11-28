<template>
  <div>
    <h1>Movie Detail</h1>
    <MovieDetail 
    v-for="result in results"
    :key="result.id"
    :result="result"/>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/counter'


import MovieDetail from '@/components/MovieDetail.vue'

const results = ref([])

const store = useMovieStore()

const API_KEY = store.API_KEY

console.log(API_KEY)


for (let num = 1; num <= 5; num++) {

  const options = {
    method: 'GET',
    url: 'https://api.themoviedb.org/3/discover/movie',
    params: {
      include_adult: 'false',
      include_video: 'false',
      language: 'ko-KR',
      page: '1',
      sort_by: 'popularity.desc',
      'vote_average.gte': '7'
    },
    headers: {
      accept: 'application/json',
      Authorization: `Bearer ${API_KEY}`
    }
  };
  
  axios
    .request(options)
    .then((res) => {
      console.log(res.data)
      // results.value = res.data.results
      res.data.results.map((obj) => {
        results.value.push(obj)
      })
    })
    .catch(err => console.error(err));
}


console.log(results.value)

</script>

<style scoped>

</style>