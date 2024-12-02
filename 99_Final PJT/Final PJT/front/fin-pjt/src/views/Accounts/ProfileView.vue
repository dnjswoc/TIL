<template>
  <div>
    <UserInfo />
  </div>
</template>

<script setup>
import UserInfo from '@/components/Profile/UserInfo.vue'
import { useRoute } from 'vue-router';

const route = useRoute()

// 해당 유저의 프로필 페이지로 갈 때 필요한 유저 id
const userId = route.params.id


</script>

<style scoped>

</style>