<template>
  <div class="community-page">
    <div class="background-image"></div>
    <div class="content-wrapper">
      <div class="header">
        <h1 class="title">{{ freearticle.title ? freearticle.title : '제목이 없습니다.' }}</h1>
        <div class="date-info">
          <small>최초 작성일: {{ formatDate(freearticle.created_at) }}</small> 
          <small>최종 수정일: {{ formatDate(freearticle.updated_at) }}</small>
        </div>
      </div>
      <hr />
      <div v-if="freearticle">
        <div class="content">
          <p>{{ freearticle.content }}</p>
        </div>
      </div>
      <hr>
      <!-- 버튼 그룹 -->
      <div class="button-group">
        <button class="edit-button" @click="goToEditPage" v-if="userStore.isOwner(freearticle.user)">⚒수정하기</button>
        <button class="delete-button" @click="deleteFreeArticle" v-if="userStore.isOwner(freearticle.user)">❌ 삭제하기</button>
        <button class="back-button" @click="back">🔙 뒤로가기</button>
      </div>
      <hr />
      <FreeArticleCommentForm />
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/community';
import { useAccountStore } from '@/stores/account';
import FreeArticleCommentForm from '@/components/Community/FreeArticle/Comment/FreeArticleCommentForm.vue';

const store = useCommunityStore();
const userStore = useAccountStore();

const route = useRoute();
const router = useRouter();
const freearticle = ref([]);

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/free_article/${route.params.free_article_id}/`,
  })
    .then((response) => {
      freearticle.value = response.data;
    })
    .catch((error) => {
      console.error('Error:', error.message, error.response?.data);
    });
});

// 날짜 및 시간 포맷팅
const formatDate = (date) => {
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  };
  return new Date(date).toLocaleString('ko-KR', options);
};

// 뒤로가기
const back = () => {
  router.push({ name: 'free_article' });
};

// 게시글 삭제
const deleteFreeArticle = () => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/free_article/${route.params.free_article_id}/`,
  })
    .then(() => {
      if (confirm('게시글을 삭제하시겠습니까?')) {
        console.log('삭제 완료!');
        router.push({ name: 'free_article' });
      }
      
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

// 수정 페이지로 이동
const goToEditPage = () => {
  router.push({ name: 'update_free_article', query: { id: route.params.free_article_id } });
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.title {
  font-family: 'Arial', sans-serif;
  font-size: 2em; /* 적당한 크기로 줄임 */
  font-weight: bold;
  font-weight: bold;
  margin: 0;
  color: #333;
}
.date-info {
  display: flex;
  flex-direction: column; /* 세로로 나란히 배치 */
  text-align: right;
  font-size: 0.9rem;
  color: #666;
}

.date-info small {
  margin: 2px; /* 세로 간격 제거 */
}

hr {
  margin: 20px 0;
  border: 1px solid #aaa;
}

.content {
  font-family: 'Arial', sans-serif;
  font-size: 2em; /* 적당한 크기로 줄임 */
  font-weight: bold;
  width: 100%; /* 너비를 컨테이너 전체로 설정 */
  max-width: 1200px; /* 최대 너비를 늘려 더 넓게 설정 */
  height: 300px; /* 고정 높이 */
  overflow: auto; /* 내용이 넘칠 경우 스크롤 표시 */
  padding: 10px; /* 내부 여백 */
  border: 1px solid #ddd; /* 테두리 추가 */
  border-radius: 5px; /* 모서리 둥글게 */
  background-color: #f9f9f9; /* 배경색 추가 */
  font-size: 1rem;
  line-height: 1.5;
  color: #333;
  margin: 0 auto; /* 화면 중앙 정렬 */
  user-select: none;
}



.community-page {
  height: 100vh; /* 뷰포트 전체 높이 */
  overflow: hidden; /* 스크롤 숨기기 */
  position: relative;
}

.content-wrapper {
  height: 100%; /* 부모 높이 전부 차지 */
  overflow-y: scroll; /* 스크롤 동작은 유지 */
  -ms-overflow-style: none; /* Internet Explorer에서 스크롤바 숨기기 */
  scrollbar-width: none; /* Firefox에서 스크롤바 숨기기 */
}

.content-wrapper::-webkit-scrollbar {
  display: none; /* Chrome, Safari에서 스크롤바 숨기기 */
}
/* 배경 이미지 */
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

/* 콘텐츠 영역 */
.content-wrapper {
  position: relative;
  background-color: rgba(255, 255, 255, 0.85);
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  max-width: 1200px;
  width: 90%;
  margin: 30px auto;
  overflow-y: auto;
  user-select: none;
}



/* 버튼 그룹 스타일 */
.button-group {
  display: flex;
  justify-content: flex-end; /* 버튼들을 오른쪽으로 정렬 */
  gap: 10px; /* 버튼 간격 */
  margin-bottom: 20px; /* 위쪽 여백 */
}

/* 버튼 공통 스타일 */
button {
  font-size: 1rem;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  font-weight: bold;
  color: white;
  user-select: none;
}

/* 수정 버튼 */
button.edit-button {
  background-color: #28a745;
}

button.edit-button:hover {
  background-color: #218838;
}

button.edit-button:active {
  background-color: #19692c;
}

/* 삭제 버튼 */
button.delete-button {
  background-color: #ff4d4f;
}

button.delete-button:hover {
  background-color: #d9363e;
}

button.delete-button:active {
  background-color: #b71d22;
}

/* 뒤로가기 버튼 */
button.back-button {
  background-color: #6c757d;
  color: white;
}

button.back-button:hover {
  background-color: #5a6268;
}

button.back-button:active {
  background-color: #4e555b;
}
</style>
