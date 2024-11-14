<template>
  <div>
    <h1>tmbd api 결과</h1>
    <RouterLink :to="{ name: 'main' }">Main</RouterLink> |
    <RouterLink :to="{ name: 'genre' }">GenreId</RouterLink>

  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<style scoped>

</style>