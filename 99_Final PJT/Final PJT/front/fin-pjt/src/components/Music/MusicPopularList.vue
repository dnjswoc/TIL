<template>
  <div class="poster-container">
    <div class="poster" @click="showMusicDetail">
      <!-- 순위 번호 표시 -->
      <div class="rank-number">Top {{ music.rank }}</div>
      <!-- 앨범 이미지 -->
      <img :src="music.album_image" alt="album_image">
      <!-- Hover 시 나타나는 정보 -->
      <div class="hover-info">
        <p>{{ music.track_name }}</p>
        <hr class="divider">
        <p>{{ music.artist_names }}</p>
      </div>
    </div>
    <MusicDetailModal 
      v-if="isModalVisible"
      @close="closeModal"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMusicStore } from '@/stores/music';
import MusicDetailModal from './MusicDetailModal.vue';

const store = useMusicStore();

const isModalVisible = ref(false); // 모달 표시 여부
const selectedMusic = ref(null); // 선택된 노래

const props = defineProps({
  music: Object, // 부모로부터 음악 데이터 받음
});

// 음악 상세 보기
const showMusicDetail = async () => {
  store.getMusicDetail(props.music.track_id); // 음악 상세 정보 가져오기
  selectedMusic.value = store.musicDetail; // 음악 상세 정보 저장
  isModalVisible.value = true; // 모달 열기
};

// 모달 닫기
const closeModal = () => {
  isModalVisible.value = false;
};
</script>

<style scoped>
.poster-container {
  flex: 0 0 auto;
  width: 300px;
  transition: transform 0.3s;
  scroll-snap-align: center;
}

.poster-container:hover {
  transform: scale(1.2);
}

.poster {
  position: relative; /* 포스터 안에 요소 배치용 */
  width: 300px; /* 포스터 너비 */
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
  font-size: 18px; /* 폰트 크기 */
  font-weight: bold; /* 텍스트 굵게 */
  padding: 5px 10px; /* 내부 여백 */
  border-radius: 10px 0 10px 0; /* 왼쪽 상단에 붙이는 느낌을 위해 한쪽만 둥글게 */
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
  padding: 10px;
  opacity: 0; /* 초기에는 보이지 않음 */
  transition: opacity 0.3s ease;
}

.poster-container:hover .hover-info {
  opacity: 1; /* 호버 시 정보 표시 */
}

.divider {
  border: none;
  border-top: 2px solid rgba(255, 255, 255, 0.7); /* 흰색 반투명 선 */
  margin: 8px 0; /* 위아래 간격 */
  width: 70%; /* 선의 길이 */
  margin-left: auto;
  margin-right: auto;
}
</style>
