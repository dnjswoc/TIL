<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <!-- v-model.trim : 양방향 바인딩 시 공백 제거 -->
        <input type="text" id="title" v-model.trim="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea id="content" v-model.trim="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import { useRouter } from 'vue-router'


const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

// DRF로 게시글 생성 요청을 보내는 함수
const createArticle = function () {
  axios({
    // 같은 django 템플릿에서 보는 것이 아니므로 csrf token을 보내지 않음
    // 보안은 다음 시간 인증과 권한에서 진행
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((res) => {
      // 게시글 생성 후 메인 페이지로 redirect
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style>

</style>
