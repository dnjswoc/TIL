<template>
  <div class="community-page">
    <div class="background-image"></div>
    <div class="content-wrapper">
      <h1 class="title">게시글 수정</h1>
      <form @submit.prevent="updateFreeArticle" class="form">
        <div class="form-group">
          <label for="title" class="form-label">제목:</label>
          <input
            type="text"
            id="title"
            v-model="freearticle.title"
            class="form-input"
            placeholder="제목을 입력해주세요."
          />
        </div>
        <div class="form-group">
          <label for="content" class="form-label">내용:</label>
          <textarea
            id="content"
            v-model="freearticle.content"
            class="form-textarea"
            placeholder="내용을 입력해주세요."
          ></textarea>
        </div>
        <div class="button-group">
          <input type="submit" class="submit-button" value="✔ 수정 완료">
          <button type="button" @click="back" class="cancel-button">❌ 수정 취소</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
// 기존 기능은 변경하지 않음
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useCommunityStore } from '@/stores/community';
import { useAccountStore } from '@/stores/account';

const store = useCommunityStore();
const userStore = useAccountStore();
const route = useRoute();
const router = useRouter();

const freearticle = ref({
  title: '',
  content: '',
  created_at: null,
  updated_at: null
});

const token = userStore.token;

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/free_article/${route.params.free_article_id}/`
  })
    .then((response) => {
      freearticle.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
});

const updateFreeArticle = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}/articles/free_article/${route.params.free_article_id}/`,
    headers: {
      Authorization: `Token ${token}`
    },
    data: {
      title: freearticle.value.title,
      content: freearticle.value.content
    }
  })
    .then(() => {
      router.push({ name: 'free_article_detail', params: { free_article_id: route.params.free_article_id } });
    })
    .catch((error) => {
      console.error(error);
    });
};

const back = function (event) {
  event.preventDefault();
  router.push({ name: 'free_article_detail', params: { free_article_id: route.params.free_article_id } });
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

.community-page {
  height: 100vh;
  overflow: hidden;
  position: relative;
  user-select: none;
}

.background-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/f.jpg'); /* 배경 이미지 경로 */
  background-size: cover;
  background-position: center;
  z-index: -1;
}

.content-wrapper {
  position: relative;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  max-width: 1200px;
  width: 90%;
  margin: 30px auto;
  overflow-y: auto;
  height: 550px;
}

.title {
  font-family: 'Arial', sans-serif;
  font-size: 2.2em; /* 적당한 크기로 줄임 */
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
  color: #333;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-size: 1rem;
  font-weight: bold;
  color: #555;
  margin-bottom: 5px;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  outline: none;
  transition: border-color 0.3s ease;
}

.form-input:focus,
.form-textarea:focus {
  border-color: #007bff;
}

.form-textarea {
  min-height: 150px;
  resize: none;
  height: 200px;
}

.button-group {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin: 0 auto;
}

.submit-button {
  background-color: #28a745;
  color: white;
  font-size: 1rem;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #218838;
}

.cancel-button {
  background-color: #ff4d4f;
  color: white;
  font-size: 1rem;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.cancel-button:hover {
  background-color: #d9363e;
}
</style>
