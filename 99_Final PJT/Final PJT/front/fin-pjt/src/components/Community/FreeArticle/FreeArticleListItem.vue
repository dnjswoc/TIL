<template>
  <div>
    <p>게시글 제목 : {{ freearticle.title? freearticle.title : '제목이 없습니다.' }}</p>
    <p>게시글 작성자 : {{ freearticle.user.nickname? freearticle.user.nickname : freearticle.user.username }}</p>
    <p>게시글 작성일 : {{ formatDate(freearticle.created_at)}}</p>
    <RouterLink :to="{name:'free_article_detail', params : {free_article_id : freearticle.id}}">디테일이다.</RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  freearticle : Object
})

// 작성일 예쁘게 출력하기 위함.
const formatDate = (date) => {
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',

  };
  return new Date(date).toLocaleString('ko-KR', options);
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

</style>