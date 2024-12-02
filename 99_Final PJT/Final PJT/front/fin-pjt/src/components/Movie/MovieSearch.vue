<template>
  <div class="top">
    <h1 class="title">Top 10 By Genre</h1>
    <MoviesGenreList 
      v-for="genre in genreList"
      :key="genre.genre_id"
      :genre="genre"
    />
    <!-- 맨 위로 가기 버튼 -->
    <button 
      v-if="showButton" 
      class="scroll-to-top" 
      @click="scrollToTop"
    >
      ↑ Top
    </button>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref, onMounted, onUnmounted } from 'vue';
import MoviesGenreList from '@/components/Movie/MoviesGenreList.vue';

const store = useMovieStore();

// 부모 view에서 저장한 장르 목록 불러오기
const genreList = store.genreList;

// 맨 위로 가기 버튼 상태
const showButton = ref(false);

// 스크롤 이벤트 핸들러
const handleScroll = () => {
  showButton.value = window.scrollY > 300; // 300px 이상 스크롤 시 버튼 표시
};

// 맨 위로 가기 함수
const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth' // 부드럽게 이동
  });
};

// 스크롤 이벤트 등록 및 해제
onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
/* 전체 컨테이너 스타일 */
.top {
  margin-top: 60px;
  padding: 20px; /* 내부 여백 */
  position: relative;
  user-select: none;
}

/* 제목 스타일 */
.title {
  position: relative; /* 배경선 위치를 조정하기 위해 */
  font-size: 3rem; /* 크기를 적당히 크게 설정 */
  text-align: center; /* 가운데 정렬 */
  margin-bottom: 20px; /* 아래 여백 */
  font-weight: bold; /* 글자를 굵게 설정 */
  color: #E63946; /* 추천 색상: 강렬한 레드 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* 그림자로 입체감 추가 */
  z-index: 5;
}

/* 제목 배경선 스타일 */
.title::after {
  content: ""; /* 빈 요소 생성 */
  position: absolute;
  left: 0; /* 왼쪽에서 시작 */
  right: 0; /* 오른쪽 끝까지 */
  bottom: 0px; /* 제목 아래로 약간 떨어뜨림 */
  height: 25px; /* 선의 굵기 */
  background-color: rgba(230, 57, 70, 0.2); /* 불투명한 색상 */
  z-index: 1; /* 텍스트 뒤로 배치 */
  border-radius: 5px; /* 둥근 모서리 */
}

/* 맨 위로 가기 버튼 스타일 */
.scroll-to-top {
  position: fixed; /* 화면에 고정 */
  bottom: 20px; /* 화면 아래에서 20px 위 */
  right: 20px; /* 화면 오른쪽에서 20px 왼쪽 */
  padding: 15px 20px; /* 버튼 크기를 더 크게 */
  font-size: 18px; /* 텍스트 크기 증가 */
  font-weight: bold;
  background-color: #e63946; /* 버튼 배경색 */
  color: white; /* 텍스트 색상 */
  border: none; /* 테두리 제거 */
  border-radius: 8px; /* 둥근 모서리 조금 더 강조 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 그림자 효과 추가 */
  cursor: pointer; /* 마우스 포인터 변경 */
  z-index: 10; /* 가장 위로 올리기 */
  transition: transform 0.2s ease, background-color 0.3s ease; /* 클릭 시 효과 */
}

/* 버튼 호버 효과 */
.scroll-to-top:hover {
  background-color: #d62839; /* 더 진한 배경색 */
  transform: scale(1.1); /* 약간 확대 효과 */
}

/* 장르 간의 간격 조정 */
.top > *:not(:last-child) {
  margin-bottom: 10px; /* 각 리스트 간 간격 */
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .title {
    font-size: 1.5rem; /* 작은 화면에서는 제목 크기 축소 */
  }
  .top {
    margin-top: 40px; /* 작은 화면에서 간격 조정 */
    padding: 10px; /* 내부 여백 축소 */
  }
}
</style>
