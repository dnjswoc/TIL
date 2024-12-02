<template>
    <teleport to="body">
    <div class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <!-- 닫기 버튼 -->
          <buttonc class="close-button" @click="closeModal" >×</buttonc>

        <!-- 모달 내부 배치 -->
        <div class="modal-body">
          <!-- 포스터 -->
          <div class="poster-container">
            <img :src="store.musicDetail.album.images[1].url" alt="poster" class="poster-img" />
          </div>

          <!-- 노래 정보 -->
          <div class="movie-details">
            <h2>{{ store.musicDetail.name }}</h2>
            <hr>
            <p><strong>아티스트 : </strong>
              <span v-for="(artist, index) in store.musicDetail.artists">
                {{ artist.name }}<span v-if="index < store.musicDetail.artists.length - 1">, </span>
              </span>
            </p>
            <p><strong>앨 범 명 :</strong> {{ store.musicDetail.album.name }}</p>
            <p><strong>발 매 일 :</strong> {{ store.musicDetail.album.release_date }}</p>
            <MusicItemYoutube />
            
          </div>
        </div>


      </div>
    </div>
  </teleport>
</template>

<script setup>
import { defineProps, defineEmits, onMounted } from 'vue';
import { useMusicStore } from '@/stores/music';
import MovieGenrePopularItemYoutube from '@/components/Movie/MovieGenrePopularItemYoutube.vue';
import MovieCommentForm from '@/components/Movie/MovieComment/MovieCommentForm.vue';
import MusicItemYoutube from './MusicItemYoutube.vue';

const store = useMusicStore();



const props = defineProps({
  isModalVisible: Boolean
})

console.log(store.musicDetail)

const emit = defineEmits();

const closeModal = () => {
  emit('close');  // 모달을 닫는 이벤트를 부모에게 전달
};

onMounted(() => {
  store.musicDetail
})


</script>

<style scoped>
.modal-overlay {
  position: fixed; /* 화면에 고정 */
  top: 0; /* 화면 상단 */
  left: 0; /* 화면 좌측 */
  width: 100vw; /* 화면 전체 너비 */
  height: 100vh; /* 화면 전체 높이 */
  background-color: rgba(0, 0, 0, 0.8); /* 더 어두운 반투명 배경 */
  display: flex; /* 중앙 정렬을 위한 flex 사용 */
  align-items: center; /* 수직 중앙 정렬 */
  justify-content: center; /* 수평 중앙 정렬 */
  z-index: 9999; /* 최상단 배치 */
}

/* 모달 본체 */
.modal-content {
  background: #1c1c1e; /* 어두운 배경 */
  border-radius: 12px; /* 부드러운 둥근 모서리 */
  max-width: 900px; /* 최대 너비 (조금 늘림) */
  width: 90%; /* 화면의 90% */
  max-height: 160vh; /* 최대 높이를 늘림 */
  overflow-y: auto;
  position: relative; /* 닫기 버튼 위치를 위해 */
  display: flex;
  flex-direction: column;
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.5); /* 부드러운 그림자 */
  color: #fff; /* 글자 색상 흰색 */
  user-select: none;
}

/* 모달 내부 배치 */
.modal-body {
  display: flex; /* 포스터와 영화 정보 가로 배치 */
  padding: 20px;
  gap: 30px; /* 간격을 조금 더 넓힘 */
  align-items: center; /* 포스터와 텍스트가 세로 중심 정렬 */
}

/* 포스터 */
.poster-container {
  flex: 1; /* 포스터 공간 */
  display: flex;
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
}

.poster-img {
  width: 100%;
  max-width: 350px; /* 포스터 크기 증가 */
  border-radius: 10px; /* 둥근 모서리 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7); /* 더 깊은 그림자 */
}

/* 노래 정보 */
.movie-details {
  flex: 3; /* 정보 공간 */
  
}

.movie-details h2 {
  margin-top: 0;
  font-size: 2rem;
  font-weight: bold;
  color: #ffd700; /* 밝은 노란색 텍스트 */
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8); /* 텍스트 그림자 */
  margin-bottom: 10px;
}

.movie-details p {
  margin-bottom: 10px;
  font-size: 1rem;
  line-height: 1.6;
  color: #ddd; /*  회색 텍스트 */
}

.movie-details strong {
  color: #fff; /* 강조 텍스트 색상 */
}


/* 닫기 버튼 */
.close-button {
  position: absolute; /* 모달 내부에서 절대 위치 */
  top: 10px; /* 위쪽에서 15px 떨어짐 */
  right: 25px; /* 오른쪽에서 15px 떨어짐 */
  background: none; /* 배경 제거 */
  border: none; /* 테두리 제거 */
  font-size: 1.8rem; /* 버튼 크기 */
  font-weight: bold; /* 두꺼운 글꼴 */
  cursor: pointer; /* 클릭 가능한 커서 */
  color: #e5e5e5; /* 기본 글자 색상 */
  transition: color 0.3s ease; /* 마우스 오버 시 부드러운 색상 변화 */
  z-index: 1000; /* 최상단에 위치 */
  user-select: none;
}

.close-button:hover {
  color: #ff3b3b; /* 마우스 오버 시 빨간색 */
}
</style>
