<template>
  <div class="movie-recommend-section">
    <!-- 추천 영화 목록 -->
    <div class="movie-card">
      <div class="movie-content">
        <p class="movie-number"># {{ index + 1 }}</p>
        <p class="movie-title" @click="showMovieDetail(movie.movie_id)">
          <strong>추천 영화</strong>: {{ movie.title }}
        </p>
        <p class="movie-reason">
          <strong>추천 이유</strong>: {{ movie.reason }}
        </p>
      </div>
      <hr class="movie-divider">
    </div>
    <!-- 영화 상세 모달 -->
    <MovieRecommendItemModal
      v-if="isModalVisible"
      :movie="selectedMovie"
      @close="closeModal"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRecommendStore } from '@/stores/recommend';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import MovieRecommendItemModal from './MovieRecommendItemModal.vue';
import axios from 'axios';

// 모달 표시 여부와 선택된 영화 정보 상태
const store = useRecommendStore()
const movieStore = useMovieStore()
const accountStore = useAccountStore()

const isModalVisible = ref(false);
const selectedMovie = ref(null);

const API_URL = 'http://127.0.0.1:8000'

// 컴포넌트의 props 정의
const props = defineProps({
  movie: Object, // 추천 영화 목록
  index : Number
});

// 영화 상세 정보를 가져오고 모달을 열기
const showMovieDetail = async (movie_id) => {
  store.getMovieDetails(props.movie.movie_id);  // 영화 상세 정보 가져오기
  selectedMovie.value = store.movieDetail;  // 영화 상세 정보 저장
  isModalVisible.value = true;  // 모달 열기
};

// 모달 닫기
const closeModal = () => {
  isModalVisible.value = false;
};
</script>

<style scoped>
.movie-recommend-section {
  margin-top: 50px;
  padding: 20px;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.9);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 10px auto;
  color: #f5f5f5;  /* 텍스트 기본 색상 */
  
}

/* 추천 영화 카드 */
.movie-card {
  background-color: #2c2c2c;  /* 어두운 배경 */
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 30px; /* 카드 간 간격 추가 */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  transition: transform 0.2s ease-in-out;
}

.movie-card:hover {
  transform: translateY(-5px);  /* 마우스 오버 시 카드가 약간 떠오르는 효과 */
}

.movie-content {
  display: flex;
  flex-direction: column;
}

.movie-number {
  font-size: 1.1rem;
  color: #ffd700;  /* 노란색 강조 */
  font-weight: bold;
  margin-bottom: 5px;
}

.movie-title {
  font-size: 1.3rem;
  color: #ff5757;  /* 강렬한 빨간색으로 클릭 가능한 느낌 강조 */
  cursor: pointer;
  margin-bottom: 10px;
}

.movie-title:hover {
  text-decoration: underline;  /* 영화 제목에 마우스를 올리면 밑줄 추가 */
}

.movie-reason {
  color: #ccc;  /* 밝은 회색으로 눈에 잘 띄게 */
  font-size: 1.1rem;
}

.movie-divider {
  margin: 15px 0;
  border: 0;
  height: 1px;
  background: #444;  /* 구분선 색상 */
}
</style>