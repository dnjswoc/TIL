<template>
  <div>
    <p>장르 id : {{ genreId.id }}</p>
    <p>장르 이름 : {{ genreId.name }}</p>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  genreId: Object
})

</script>

<style scoped>

</style>