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
import { useMovieStore } from '@/stores/counter'

import GenreItem from '@/components/GenreItem.vue'

const genreIds = ref([])

const store = useMovieStore()

const options = {
  method: 'GET',
  url: 'https://api.themoviedb.org/3/genre/movie/list',
  params: {language: 'ko'},
  headers: {
    accept: 'application/json',
    Authorization: `Bearer ${store.API_KEY}`
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