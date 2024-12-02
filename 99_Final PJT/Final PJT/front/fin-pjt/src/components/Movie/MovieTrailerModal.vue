<template>
  <div v-if="isVisible" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <iframe
        :src="videoUrl"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen
        class="trailer-iframe"
      ></iframe>
      <button @click="close" class="close-btn">닫기</button>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  isVisible: Boolean, // 모달 표시 여부
  videoUrl: String,   // YouTube 예고편 URL
});

const emit = defineEmits(['close']); // 부모에게 닫기 이벤트 전달

const close = () => {
  emit('close');
};
</script>

<style scoped>
/* 모달 오버레이: 어두운 배경 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.9); /* 짙은 검은색 배경 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

/* 모달 컨텐츠 */
.modal-content {
  background: #1e1e1e; /* 어두운 회색 배경 */
  padding: 20px;
  border-radius: 12px; /* 부드러운 모서리 */
  max-width: 800px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.8); /* 그림자 효과 */
  display: flex;
  flex-direction: column;
  align-items: center; /* 중앙 정렬 */
}

/* 유튜브 영상 Iframe */
.trailer-iframe {
  width: 100%;
  height: 450px;
  border: none;
  border-radius: 8px; /* 비디오의 둥근 모서리 */
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.7); /* 비디오에 그림자 추가 */
}

/* 닫기 버튼 */
.close-btn {
  margin-top: 18px; /* 위쪽 여백 */
  background-color: #e50914; /* 넷플릭스 스타일의 빨간 버튼 */
  color: white;
  border: none;
  border-radius: 8px; /* 부드러운 모서리 */
  padding: 10px 16px; /* 버튼 크기 */
  font-size: 1.1rem; /* 텍스트 크기 */
  font-weight: bold; /* 텍스트 강조 */
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease; /* 부드러운 애니메이션 */
}

/* 닫기 버튼 마우스 오버 효과 */
.close-btn:hover {
  background-color: #b00710; /* 어두운 빨간색 */
  transform: scale(1.05); /* 살짝 확대 */
}

/* 닫기 버튼 클릭 효과 */
.close-btn:active {
  background-color: #8a000c; /* 더 어두운 빨간색 */
  transform: scale(0.95); /* 살짝 축소 */
}

/* 스크롤바 스타일 */
.modal-content::-webkit-scrollbar {
  width: 8px;
}

.modal-content::-webkit-scrollbar-thumb {
  background: #555; /* 스크롤바 색상 */
  border-radius: 4px;
}

.modal-content::-webkit-scrollbar-thumb:hover {
  background: #777; /* 호버 시 스크롤바 색상 */
}

.modal-content::-webkit-scrollbar-track {
  background: #1e1e1e; /* 스크롤 트랙 색상 */
}
</style>



