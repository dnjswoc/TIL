<template>
  <div class="poster-container">
    <div class="poster" @click="showMovieDetail">
      <div class="rank-number">Top {{ index + 1 }}</div>
      <img :src="posterUrl + movie.poster_path" alt="Movie Poster" class="poster-img"/>
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
import MovieGenrePopularItemModal from '@/components/Movie/MovieGenrePopularItemModal.vue';

// 장르별 인기 영화 목록을 반복하며 영화 한 편을 prop 받음
const props = defineProps({
  movie: Object,
  index: Number
});

// 스토어 및 상태 관리
const store = useMovieStore();
const posterUrl = store.posterUrl;

// 참조를 위한 ref
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
  position: relative;
  display: inline-block;
  margin-right: 5px; /* 포스터 간격을 주기 위해 오른쪽 여백 추가 */
}



.poster {
  display: inline-block;
  width: 200px;  /* 포스터의 고정 너비 */
  height: 300px;  /* 포스터의 고정 높이 */
  overflow: hidden;  /* 이미지가 넘치지 않도록 숨김 처리 */
  transition: transform 0.3s ease;  /* 포스터가 부드럽게 커지는 애니메이션 */
}

.poster-img {
  width: 100%;  /* 포스터 너비에 맞게 이미지 크기 조정 */
  height: 100%;  /* 포스터 높이에 맞게 이미지 크기 조정 */
  object-fit: cover;  /* 이미지 비율을 유지하면서 영역을 채우기 */
  transition: transform 0.3s ease;  /* 이미지 크기 변화에 대한 부드러운 애니메이션 */
  border-radius: 10px; /* 포스터에 둥근 모서리 추가 */
}

.poster:hover .poster-img {
  transform: scale(1.1);  /* 마우스를 올렸을 때 이미지 크기를 20% 확대 */
}

.poster:hover {
  transform: scale(1.1);  /* 포스터 전체 크기 확대 */
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