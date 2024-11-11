<template>
  <div>
    <h1>UserView</h1>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>


    <h2>{{ $route.params }}번 유저 프로필 페이지</h2>
    <!-- style guide에서 권장하지는 않음. 코드 가독성의 이유로 -->
    <h2>{{ $route.params.id }}번 유저 프로필 페이지</h2>
    <h2>{{ userId }}번 유저 프로필 페이지</h2>
    <button @click="goHome">홈으로!</button>
    <button @click="routeUpdate">100번 유저 페이지로!</button>

    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

import { ref } from 'vue'

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()

const goHome = function () {
  // router.push({ name: 'home' })
  router.replace({ name: 'home' })
}

onBeforeRouteLeave((to, from) => {
  // confirm : 팝업창(yes : true, no : false)
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

const routeUpdate = function () {
  router.push({ name: 'user', params: { id: 100 }})
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.Id
})


</script>

<style scoped>

</style>