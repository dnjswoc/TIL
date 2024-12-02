<template>
    <div class="community-page">
      <div class="background-image"></div>
      <div class="content-wrapper">
        <button class="create-button" @click="goToCreatePage">✏게시글 작성</button>
        <FreeArticleList />
      </div>
    </div>
  </template>
  
  <script setup>
  import FreeArticleList from '@/components/Community/FreeArticle/FreeArticleList.vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  const goToCreatePage = () => {
    router.push({ name: 'free_article_create' });
  };
  </script>
  
  <style scoped>
  .community-page {
    position: relative;
    height: 100vh;
    overflow: hidden;
  }
  
  /* 배경 이미지 스타일 */
  .background-image {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('@/assets/f.jpg');
    background-size: cover;
    background-position: center;
    z-index: -1;
  }
  
  .content-wrapper {
    position: relative;
    background-color: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
    max-width: 1600px;
    width: 90%;
    margin: auto;
    height: 600px;
    overflow-y: auto;
  
    margin-top: 30px; /* 상단 메뉴와 겹치지 않도록 여백 추가 */
  }
  
  /* 게시글 작성 버튼 스타일 */
  .create-button {
    position: absolute;
    top: 20px;
    right: 60px;
    background-color: #151314;
    color: white;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 15px 30px;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    transition: background-color 0.3s ease, transform 0.2s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }
  
  .create-button:hover {
    background-color: #2e2e2e;
    transform: scale(1.05);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  }
  
  .create-button:active {
    background-color: #003d82;
    transform: scale(0.98);
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
  }
  </style>
  