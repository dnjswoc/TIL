<template>
  <h1>App.Vue</h1>
  <MyComponent />
</template>


<script setup>
// 상대 경로로 import
// import MyComponent from './components/MyComponent.vue'

// @ - src를 뜻하는 약어, 절대 경로로 import
import MyComponent from '@/components/MyComponent.vue'

</script>

<style scoped>
/* 태그 선택자를 쓰면 자식 컴포넌트의 최상위까지는 CSS가 적용된다 */
/* 따라서 태그 선택자가 아니라 클래스 선택자를 쓰는 것이 좋다. */
div {
  border: 1px solid black;
}

</style>
