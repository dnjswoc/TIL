<template>
  <div class="community-page">
    <div class="background-image"></div>
    <div class="content-wrapper">
      <h1 class="title">게시글 작성</h1>
      <form @submit.prevent="createFreeArticle" class="form">
        <div class="form-group">
          <label for="title" class="form-label">제목:</label>
          <input
            type="text"
            id="title"
            v-model="title"
            class="form-input"
            placeholder="제목을 입력해주세요."
          />
        </div>
        <div class="form-group">
          <label for="content" class="form-label">내용:</label>
          <textarea
            id="content"
            v-model="content"
            class="form-textarea"
            placeholder="내용을 입력해주세요."
          ></textarea>
        </div>
        <div class="button-group">
          <input type="submit" class="submit-button" value="✔ 게시글 작성">
          <button type="button" @click="goBackFreeArticlePage" class="cancel-button">❌ 작성 취소</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useCommunityStore } from '@/stores/community';
import { useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account';

const store = useCommunityStore();
const router = useRouter();

const userStore = useAccountStore();
const token = userStore.token;

const title = ref(null);
const content = ref(null);

const createFreeArticle = function () {
  axios({
    method: 'POST',
    url: `${store.API_URL}/articles/free_article/comment/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${token}`,
    },
  })
    .then(() => {
      router.push({ name: 'free_article' });
    })
    .catch((error) => {
      console.log(error);
      console.log('Error message:', error.message);
      console.log('Response data:', error.response?.data);
      console.log('Response status:', error.response?.status);
      console.log('Request:', error.config);
    });
};

const goBackFreeArticlePage = function () {
  router.push({ name: 'free_article' });
};
</script>

<style scoped>
.community-page {
  height: 100vh;
  overflow: hidden;
  position: relative;
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
  font-size: 2rem;
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
  font-size: 1.3rem;
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
  user-select: none;
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
