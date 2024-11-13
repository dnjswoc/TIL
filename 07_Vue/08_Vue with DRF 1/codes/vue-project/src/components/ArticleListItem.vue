<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  article: Object
})

</script>
