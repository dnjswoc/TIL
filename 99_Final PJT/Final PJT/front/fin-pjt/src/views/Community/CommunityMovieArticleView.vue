<template>
  <h1>영화게시판이다.</h1>
  <button @click="goToCreatePage">게시글 작성</button>
  <MovieArticleList />

</template>

<script setup>
import MovieArticleList from '@/components/Community/MovieArticle/MovieArticleList.vue';
import { useRouter } from 'vue-router'


const router = useRouter()

const goToCreatePage = function () {
  router.push({name : 'free_article_create'})
}


</script>
<style scoped>

</style>