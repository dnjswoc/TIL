<!-- vue 작성하면 자동완성이 뜬다. -->
<!-- 하나의 파일에 template, script, style 모두 작성 -->
<template>
  <div class="greeting">
    {{  }}
  </div>
</template>

<script setup>
// const { ref } = Vue => 구조분해 할당은 더 이상 쓰지 않는다.
// import로 구조분해 할당 해준다.
import { ref } from 'vue'

const msg = ref('hello')

// return {} => return도 필요 없어졌다. 바로 사용 가능

</script>


<!-- scoped : 해당 파일에만 style을 적용하도록 한다. -->
<style scoped>
.greeting {
  color: red;
}

</style>