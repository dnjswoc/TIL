<template>
  <div class="userinfo-container" v-if="userInfo">
    <div class="profile-wrapper">
      <div class="profile-content">
        <!-- <p>ID : {{ userInfo.username }}</p> -->
        <p>{{ userInfo.nickname }}님 반갑습니다!</p>
        <div v-if="userInfo.genre1.trim() !== '' || userInfo.genre2.trim() !== ''">
          <p>선호하는 노래 장르 : {{ userInfo.genre1 }}
            <span v-if="userInfo.genre1.trim() !== '' && userInfo.genre2.trim() !== ''">, </span>
            {{ userInfo.genre2 }}</p>
        </div>
        <div class="empty-genre" v-else>
          <p>좋아하는 장르를 기록해보세요! 🎧</p>
        </div>
        <div v-if="userInfo.introduction.trim() !== ''">
          <p>소개글 : {{ userInfo.introduction }}</p>
        </div>
        <div v-else>
          <p>소개글을 작성해 보는 건 어떤가요?</p>
        </div>
        
        <RouterLink 
          :to="{ name : 'profileUpdate' }"
          v-if="userInfo.id === userId.id"
          :class="edit-profile-link"
          style="text-decoration:none;"
        >
          <div class="edit-profile-item">
            <span class="edit-profile-icon">✍</span>
            <span>회원정보 수정하기</span>
          </div>
        </RouterLink>
        

      </div>
      <div class="liked-movies">
        <h3>{{ userInfo.nickname }}님이 좋아하는 Movie 😍</h3>
        <div class="movies-grid" v-if="userInfo">
          <UserLikeMovie 
            v-for="movie in paginatedMovies"
            :key="movie.movie_id"
            :movie="movie"
          />
        </div>
        <div class="pagination-controls" v-if="totalPages > 0">
          <button @click="prevPage" :disabled="currentPage === 1">이전</button>
          <span>페이지 {{ currentPage }} / {{ totalPages }}</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
        </div>
        <div class="else" v-else>
          <p>좋아요를 남긴 영화가 없어요...</p>
          <p>영화에 좋아요를 남겨보세요!</p>
          <RouterLink 
            :to="{ name : 'movies' }"
            :class="edit-profile-link"
            style="text-decoration:none;"
          >
            <div class="edit-profile-item">
              <span class="edit-profile-icon">🎥</span>
              <span>영화 보러가기!</span>
            </div>
          </RouterLink>
        </div>
        </div>
      </div>
    </div>
  
  <RouterView />
</template>

<script setup>
import { useAccountStore } from '@/stores/account'
import { ref, onMounted, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { RouterLink, RouterView } from 'vue-router'
import UserLikeMovie from './UserLikeMovie.vue'


const store = useAccountStore()

// 로그인 한 유저의 정보를 가져오기
const userId = store.userId

const { userInfo } = storeToRefs(store)
// console.log(userInfo)

const currentPage = ref(1);
const moviesPerPage = 4;

const totalPages = computed(() => {
  return userInfo.value && userInfo.value.like_movies
    ? Math.ceil(userInfo.value.like_movies.length / moviesPerPage)
    : 0;
});

const paginatedMovies = computed(() => {
  if (userInfo.value && userInfo.value.like_movies) {
    const start = (currentPage.value - 1) * moviesPerPage;
    const end = start + moviesPerPage;
    return userInfo.value.like_movies.slice().reverse().slice(start, end);
  }
  return [];
});


const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

// 테스트 결과 유저 데이터 잘 나옴ㅎㅎ
onMounted(() => {
  store.getProfile()
})


</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

.userinfo-container {
  
  color: #fff;
  background-color: #121212;
  font-family: 'Arial', sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  user-select: none;
}


.profile-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 600px;
  margin-top: 100px;
}

.profile-content {
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  font-size: 1.2rem; /* 적당한 크기로 줄임 */
  font-weight: bold;
  padding: 20px;
  background-color: #181818;
  border-radius: 10px;
  width: 100%;
  text-align: left;
  margin-bottom: 20px;
}

.liked-movies {
  font-family: 'Arial', sans-serif;
  font-size: 1.1rem; /* 적당한 크기로 줄임 */
  font-weight: bold;
  padding: 20px;
  background-color: #181818;
  border-radius: 10px;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.liked-movies h3{
  font-family: 'Arial', sans-serif;
  font-size: 1.5rem; /* 적당한 크기로 줄임 */
  font-weight: bold;
}

.movies-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 5px;
  gap: 45px;
  width: 100%;
}

.movie-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pagination-controls {
  display: flex;
  justify-content: space-between;
  width: 100%;
  max-width: 800px;
  margin-top: 20px;
}

button {
  font-family: 'Arial', sans-serif;
  font-size: 1.2rem; /* 적당한 크기로 줄임 */
  font-weight: bold;
  background-color: #1db954;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 50px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:disabled {
  background-color: #555;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #1ed760;
}

.else {
  width:100%;
}


.edit-profile-link {
  color: inherit;
  text-decoration: none;
}


.edit-profile-item {
  display: flex;
  align-items: center;
  margin-top: 20px;
  padding: 10px;
  background-color: #333;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  text-decoration: none;
  color:#fff
}

.edit-profile-item:hover {
  background-color: #444;
}

.edit-profile-icon {
  width: 24px;
  height: 24px;
  margin-bottom: 5px;
  margin-left: 6px;
  background: url('/path/to/edit-icon.svg') no-repeat center center;
  background-size: contain;
  margin-right: 10px;
}

.empty-genre {
  margin-top: 10px;
  margin-bottom: 10px;
  padding-top:5px;
  /* padding-bottom:5px; */
}


</style>