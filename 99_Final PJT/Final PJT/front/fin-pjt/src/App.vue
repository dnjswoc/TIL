<template>
  <AppNavbar />
  <RouterView />
</template>

<script setup>
import AppNavbar from '@/components/Common/AppNavbar.vue'

</script>

<style scoped>
body {
  background-color: #151314; /* 메인 배경색 */
  color: #ffffff; /* 텍스트 기본 색상 */
  margin: 0;
  padding: 0;
}
</style>