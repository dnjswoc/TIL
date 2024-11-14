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


import MovieDetail from '@/components/MovieDetail.vue'

const results = ref([])


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
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMTY1YWYwNGVmODA3YmNmZTJjMzMxZDU5ZjAwODk5YSIsIm5iZiI6MTczMTU2Nzg2OS4wMDMxNjc0LCJzdWIiOiI2NzMzMTA3NWJjNzhjZTJiOTRiYTRlYTkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.zDAyiZEt3JDmLJtHfcIJMsyszLP0pwVvJLn4O_SsRhA'
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