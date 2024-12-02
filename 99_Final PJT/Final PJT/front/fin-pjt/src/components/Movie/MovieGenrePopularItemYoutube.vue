<template>
  <div>
    <button @click="openTrailer">영화 예고편 🎬</button>
    <MovieTrailerModal
      v-if="isTrailerModalVisible"
      :videoUrl="trailerUrl"
      :isVisible="isTrailerModalVisible"
      @close="closeTrailerModal"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import MovieTrailerModal from '@/components/Movie/MovieTrailerModal.vue';

const store = useMovieStore();
const isTrailerModalVisible = ref(false); // 모달 표시 여부
const trailerUrl = ref(''); // YouTube 예고편 URL

const openTrailer = async () => {
  const url = await store.getMovieTrailer();
  if (url) {
    trailerUrl.value = url;
    isTrailerModalVisible.value = true; // 모달 열기
  } else {
    alert('예고편을 찾을 수 없습니다.');
  }
};

const closeTrailerModal = () => {
  isTrailerModalVisible.value = false;
};
</script>

<style scoped>
/* 컨테이너를 오른쪽 정렬 */
div {
  text-align: right; /* 버튼을 오른쪽으로 정렬 */
}

/* 영화 예고편 보기 버튼 */
button {
  padding: 12px 24px; /* 버튼 내부 여백 */
  font-size: 1.2rem; /* 버튼 텍스트 크기 */
  font-weight: bold; /* 두꺼운 텍스트 */
  color: #ffffff; /* 텍스트 색상: 흰색 */
  background-color: #e50914; /* 넷플릭스 스타일 빨간색 */
  border: none; /* 테두리 제거 */
  border-radius: 8px; /* 부드러운 모서리 */
  cursor: pointer; /* 클릭 가능한 커서 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4); /* 그림자 추가 */
  transition: background-color 0.3s ease, transform 0.3s ease; /* 부드러운 애니메이션 */
}

/* 버튼 마우스 오버 효과 */
button:hover {
  background-color: #b00710; /* 어두운 빨간색 */
  transform: scale(1.1); /* 살짝 확대 */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.6); /* 그림자 강화 */
}

/* 버튼 클릭 시 효과 */
button:active {
  background-color: #8a000c; /* 더 어두운 빨간색 */
  transform: scale(1.05); /* 약간 축소 */
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.4); /* 그림자 축소 */
}
</style>
