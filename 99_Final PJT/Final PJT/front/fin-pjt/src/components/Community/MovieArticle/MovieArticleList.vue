<template>
  <div>
    <h2>MovieArticle List</h2>
    <FreeArticleListItem 
    v-for="freearticle in store.freearticles"
    :key="freearticle.id"
    :freearticle="freearticle"
    />
  </div>
</template>

<script setup>
import FreeArticleListItem from '@/components/Community/FreeArticle/FreeArticleListItem.vue';
import MovieArticleListItem from '@/components/Community/MovieArticle/MovieArticleList.vue';
import { useCommunityStore } from '@/stores/community';
import { onMounted } from 'vue';

const store = useCommunityStore()

onMounted(() => {
  store.getMovieArticles()
})

</script>

<style scoped>

</style>