<template>
  <div>
    <h2>MyComponent</h2>
    <MyComponentItem />
    <MyComponentItem />
    <MyComponentItem />
    <!-- <MyComponentItem
      v-for=""
    /> 나중에는 이렇게 작성 가능 -->
  </div>
</template>

<script setup>
import MyComponentItem from '@/components/MyComponentItem.vue'

</script>

<style scoped>

</style>