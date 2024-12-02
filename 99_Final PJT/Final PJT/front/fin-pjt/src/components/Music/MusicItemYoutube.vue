<template>
  <div>
  <div class="button-container">
    <button @click="openTrailer" class="youtube-button">🎵 뮤직비디오</button>
  </div>
    <MusicVideoModal
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
import { useMusicStore } from '@/stores/music';
import MovieTrailerModal from '@/components/Movie/MovieTrailerModal.vue';
import MusicVideoModal from './MusicVideoModal.vue';

const store = useMusicStore();
const isTrailerModalVisible = ref(false); // 모달 표시 여부
const trailerUrl = ref(''); // YouTube 예고편 URL

const openTrailer = async () => {
  const url = await store.getMusicVideo();
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
/* 버튼 컨테이너 */
.button-container {
  display: flex;
  gap: 10px; /* 버튼 간 간격 */
  margin-top: 20px; /* 버튼 위쪽 간격 */
  justify-content: flex-end; /* 버튼을 오른쪽으로 정렬 */
}

.youtube-button {
  background-color: #e50914; /* 빨간색 버튼 */
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 5px; /* 아이콘과 텍스트 간 간격 */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* 버튼 그림자 */
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.youtube-button:hover {
  background-color:#b00710;/* 호버 시 더 짙은 빨간색 */
  transform: scale(1.1); /* 살짝 확대 */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.6); /* 그림자 강화 */
}

/* 버튼 클릭 시 효과 */
.youtube-button:active {
  background-color: #8a000c; /* 더 어두운 빨간색 */
  transform: scale(1.05); /* 약간 축소 */
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.4); /* 그림자 축소 */
}

.youtube-button svg {
  width: 20px;
  height: 20px;
  fill: white; /* 아이콘 색상 */
}
</style>