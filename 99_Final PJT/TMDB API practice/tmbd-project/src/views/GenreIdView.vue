<template>
  <div>
    <h1>Genre List</h1>
    <GenreItem
      v-for="genreId in genreIds"
      :key="genreId.id"
      :genre-id="genreId"
    />
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

import GenreItem from '@/components/GenreItem.vue'

const genreIds = ref([])

const options = {
  method: 'GET',
  url: 'https://api.themoviedb.org/3/genre/movie/list',
  params: {language: 'ko'},
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMTY1YWYwNGVmODA3YmNmZTJjMzMxZDU5ZjAwODk5YSIsIm5iZiI6MTczMTU5MDQ2NS44NTk2NTQyLCJzdWIiOiI2NzMzMTA3NWJjNzhjZTJiOTRiYTRlYTkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Dcq4HYC4XLkmOYkkN9-Q4acPTafIy9ZAE3xBGBKU8Ag'
  }
};

axios
  .request(options)
  .then((res) => {
    console.log(res.data)
    genreIds.value = res.data.genres
  })
  .catch(err => console.error(err));

</script>

<style scoped>

</style>