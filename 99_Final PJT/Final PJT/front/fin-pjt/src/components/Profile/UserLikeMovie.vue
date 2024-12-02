<template>
  <div class="poster-container">
    <div class="poster" @click="showMovieDetail">
      <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" alt="Movie Poster">
      <div class="hover-info">
        <p>{{ movie.title }}</p>
        <hr class="divider">
        <p>{{ movie.genre1 }} / {{ movie.genre2 }}</p>
      </div>
    </div>
    <MovieGenrePopularItemModal 
      v-if="isModalVisible"
      @close="closeModal"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import MovieGenrePopularItemModal from '../Movie/MovieGenrePopularItemModal.vue';




const props = defineProps({
  movie: Object
})


const store = useMovieStore();
const posterUrl = store.posterUrl;

const isModalVisible = ref(false);  // 모달 표시 여부
const selectedMovie = ref(null);  // 선택된 영화

// 영화 상세 정보를 가져오고 모달을 열기
const showMovieDetail = async (movie_id) => {
  store.getMovieDetail(props.movie.movie_id);  // 영화 상세 정보 가져오기
  selectedMovie.value = store.movieDetail;  // 영화 상세 정보 저장
  isModalVisible.value = true;  // 모달 열기
};

// 모달 닫기
const closeModal = () => {
  isModalVisible.value = false;
};
</script>

<style scoped>
.poster-container {
  flex: 0 0 auto;
  width: 200px; /* 포스터 너비 */
  transition: transform 0.3s;
  scroll-snap-align: center;
}

.poster-container:hover {
  transform: scale(1.05);
}

.poster {
  position: relative; /* 포스터 안에 요소 배치용 */
  width: 200px; /* 포스터 너비 */
  height: 300px; /* 포스터 높이 */
}

.poster img {
  width: 100%; /* 포스터 너비를 컨테이너에 맞춤 */
  height: 100%; /* 포스터 높이를 컨테이너에 맞춤 */
  object-fit: cover; /* 이미지 비율을 유지하며 영역 채움 */
  border-radius: 10px; /* 둥근 모서리 */
}

.rank-number {
  position: absolute;
  top: 0; /* 위쪽 끝에 딱 붙임 */
  left: 0; /* 왼쪽 끝에 딱 붙임 */
  background-color: rgba(128, 128, 128, 1); /* 회색 박스, 약간 투명 */
  color: white; /* 텍스트 색상 */
  font-size: 16px; /* 포스터 크기에 맞게 폰트 크기 조정 */
  font-weight: bold; /* 텍스트 굵게 */
  padding: 4px 8px; /* 내부 여백 */
  border-radius: 10px 0 10px 0; /* 왼쪽 상단에 둥근 모서리 */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5); /* 살짝 그림자 추가 */
  z-index: 1; /* 다른 요소 위에 표시 */
}

.hover-info {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(0, 0, 0, 0.8); /* 반투명 검은 배경 */
  color: white;
  text-align: center;
  padding: 4px; /* 포스터 크기에 맞게 패딩 조정 */
  opacity: 0; /* 초기에는 보이지 않음 */
  transition: opacity 0.3s ease;
  font-size: 12px;
}

.hover-info p:first-child {
margin-top: 10px; /* 제목과 위쪽의 간격 설정 */
}

.poster-container:hover .hover-info {
  opacity: 1; /* 호버 시 정보 표시 */
}

.divider {
  border: none;
  border-top: 2px solid rgba(255, 255, 255, 0.7); /* 흰색 반투명 선 */
  margin: 4px 0; /* 위아래 간격 */
  width: 60%; /* 영화 크기에 맞게 선 길이 조정 */
  margin-left: auto;
  margin-right: auto;
}
</style>

