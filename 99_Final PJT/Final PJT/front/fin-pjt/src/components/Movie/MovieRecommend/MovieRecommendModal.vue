<template>
  <div class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <!-- 닫기 버튼 -->
      <button class="close-button" @click="closeModal">×</button>

      <!-- 모달 내부 배치 -->
      <div class="modal-body">
        <!-- 타이핑 효과 제목 -->
        <h3 class="typing-title">{{ displayedTitle }}</h3>
        <br>
        <!-- 검색 폼 -->
          <form @submit.prevent="handleSearch">
            
            <!-- 검색 입력 -->
            <input
              v-model="music_genre"
              type="text"
              placeholder="좋아하는 노래나 장르를 입력해보세요!"
              required
            />
            <!-- 검색 버튼 -->
            <button type="submit" :disabled="isLoading" class="sub-btn">
              {{ isLoading ? "검색 중..." : "검색" }}
            </button>
          </form>
          <!-- 예시 텍스트 -->
          <p class="example-text">예시 : 발라드, Pop, Jazz, BTS, Coldplay, 아델의 'Hello'</p>

          <div v-if="isLoading" class="loading-gif-container">
            <img :src="loadingGif" alt="로딩 중" />
            <p>파이리가 열심히 불을 지피는 중이에요... 잠시만 기다려주세요!</p>
          </div>
        <!-- 검색 결과 -->
        <div v-if="!isLoading && movieRecommendList?.length > 0">
          <hr>
          <h4 class="sub-title">🎼 음악과 함께 떠나는 영화 여행 🎞 </h4>
          <MovieRecommendList 
            v-for="(movie, index) in movieRecommendList"
            :key="index"
            :movie="movie"
            :index="index"
          />
        </div>

        <!-- 검색 결과가 없을 때 -->
        <div v-else-if="!isLoading && isSearched && movieRecommendList?.length === 0">
          <p>검색 결과가 없습니다.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useRecommendStore } from '@/stores/recommend';
import MovieRecommendList from './MovieRecommendList.vue';
import loadingGif from '@/assets/loading.gif';

const store = useRecommendStore();


// 상태
const music_genre = ref('');
const isLoading = ref(false); // 로딩 상태
const isSearched = ref(false); // 검색 실행 여부
const movieRecommendList = ref([]);

// 타이핑 효과 관련 상태
const fullTitle = "🎧 멜로디에서 영화로 이어지는 감동을 느껴보세요.";
const displayedTitle = ref('');
const typingSpeed = 85; // 타이핑 속도(ms)

// 타이핑 효과 함수
const typeTitle = () => {
  let index = 0;
  const typingInterval = setInterval(() => {
    if (index < fullTitle.length) {
      displayedTitle.value += fullTitle[index];
      index++;
    } else {
      clearInterval(typingInterval); // 타이핑 완료 시 인터벌 정지
    }
  }, typingSpeed);
};

onMounted(() => {
  typeTitle(); // 모달이 열릴 때 타이핑 효과 시작
});

const handleSearch = async () => {
  if (!music_genre.value.trim()) return;

  // 로딩 상태 시작
  isLoading.value = true;
  isSearched.value = true;

  // 이전 데이터 초기화
  movieRecommendList.value = [];

  try {
    // 2초 대기 (API 호출 시뮬레이션)
    await new Promise((resolve) => setTimeout(resolve, 13000));

    // 실제 API 호출
    const response = await store.getMovieRecommend(music_genre.value);

    // Vue의 렌더링 사이클과 동기화
    setTimeout(() => {
      movieRecommendList.value = response;
    }, 0);
  } catch (error) {
    console.error("API 호출 중 오류:", error);
  } finally {
    // 로딩 상태 종료
    isLoading.value = false;
  }
};




// 검색 상태 감시
watch(() => store.movieRecommendList, (newList) => {
  movieRecommendList.value = newList; // 데이터가 바뀌면 즉시 반영
});

const emit = defineEmits();

const closeModal = () => {
  emit('close'); // 모달을 닫는 이벤트를 부모에게 전달
};
</script>

<style scoped>
/* 모달 배경 설정 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9); /* 어두운 반투명 배경 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

/* 모달 본체 */
.modal-content {
  background: #1e1e1e; /* 어두운 배경 */
  border-radius: 16px;
  max-width: 1000px; /* 최대 너비 */
  width: 90%; /* 화면의 90% */
  max-height: 85vh; /* 최대 높이 */
  overflow-y: auto;
  position: relative; /* 닫기 버튼 위치를 위해 */
  display: flex;
  flex-direction: column;
  padding: 20px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6); /* 그림자 효과 */
  color: #f5f5f5; /* 기본 텍스트 색상 */
  user-select: none;
}

.sub-btn{
  font-weight: bold;
}

/* 모달 내부 배치 */
.modal-body {
  padding: 20px;
  gap: 20px;
}

.recommendation-container {
  min-height: 300px; /* 목록 영역에 최소 높이 지정 */
  display: flex;
  flex-direction: column;
  justify-content: center; /* 로딩 중일 때 가운데 정렬 */
  align-items: center;
}

/* 제목 스타일 */
.typing-title {
  color: #ffd700; /* 밝은 노란색 */
  text-align: center;
  font-size: 1.8rem;
  margin-bottom: 20px;
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);
  white-space: pre-wrap; /* 줄바꿈 허용 */
  font-weight: bold;
}

/* 검색 입력 */

form {
  display: flex;
  justify-content: center; /* 수평 가운데 정렬 */
  align-items: center; /* 수직 가운데 정렬 */
  
  gap: 20px; /* 입력 필드와 버튼 간격 */
}

input {
  width: 700px;
  padding: 10px;
  margin-right: 5px;
  border: 1px solid #444;
  border-radius: 4px;
  font-size: 16px;
  color: #f5f5f5; /* 텍스트 색상 */
  background: #333; /* 입력 필드 배경색 */
  letter-spacing: 0.07em; /* 글자 간격 추가 */
}

input::placeholder {
  color: #aaa; /* 플레이스홀더 색상 */
}

.example-text {
  color: #aaa; /* 회색 텍스트 */
  font-size: 0.9rem; /* 작은 크기 */
  margin-top: 10px; /* 입력폼과 간격 */
  text-align: center; /* 중앙 정렬 */
  font-style: italic; /* 이탤릭체로 친근함 강조 */
}


/* 검색 버튼 */
button {
  padding: 15px 25px;
  background-color: #e50914; /* 넷플릭스 빨간색 */
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #b00710; /* 어두운 빨간색 */
  transform: scale(1.05); /* 살짝 확대 */
}

button:disabled {
  background-color: #555; /* 비활성화 버튼 색상 */
  cursor: not-allowed; /* 커서 비활성화 */
}

/* 로딩 중 메시지 */
.loading {
  color: #ffd700; /* 밝은 노란색 */
  text-align: center;
  margin-top: 20px;
  font-size: 1.2rem;
}

.loading-gif-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.9); /* 반투명 배경 */
  padding: 20px;
  border-radius: 8px;
  color: white;
  z-index: 9999 !important; /* 최상단 표시 */
  display: flex; /* 내부 요소들을 가운데 배치하기 위한 flex 설정 */
  flex-direction: column; /* 세로 방향 배치 */
  justify-content: center; /* 수직 방향 가운데 정렬 */
  align-items: center; /* 수평 방향 가운데 정렬 */
}


.sub-title {
  text-align: center; /* 텍스트를 중앙으로 정렬 */
  width: 100%; /* 요소가 전체 너비를 차지하게 설정 */
  margin: 20px 0; /* 위아래 여백을 20px 설정 */
  font-size: 1.5rem; /* 텍스트 크기를 크게 설정하여 시인성 향상 */
  font-weight: bold; /* 두꺼운 글씨체로 강조 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 그림자 효과로 입체감 추가 */
  letter-spacing: 0.05em; /* 글자 사이 간격을 조금 넓혀 가독성 향상 */
  padding: 10px; /* 제목 주위에 여백을 추가하여 공간감을 줌 */
  display: block; /* 요소를 블록 요소로 변경 */
}


/* 닫기 버튼 */
.close-button {
  position: absolute; /* 모달 내부에서 절대 위치 */
  top: 10px; /* 위쪽에서 10px 떨어짐 */
  right: 25px; /* 오른쪽에서 25px 떨어짐 */
  background: none; /* 배경 제거 */
  border: none; /* 테두리 제거 */
  font-size: 2rem; /* 버튼 크기 */
  font-weight: bold; /* 두꺼운 글꼴 */
  cursor: pointer; /* 클릭 가능한 커서 */
  color: #e5e5e5; /* 기본 글자 색상 */
  transition: color 0.3s ease; /* 색상 변화 애니메이션 */
  z-index: 1000; /* 최상단에 위치 */
}

/* 마우스 오버 시 */
.close-button:hover {
  color: #ff3b3b; /* 마우스 오버 시 빨간색 */
  background: none; /* 배경 제거 */
}

/* 클릭 시 */
.close-button:active {
  color: #ff0000; /* 클릭 시 더 짙은 빨간색 */
  background: none; /* 배경 제거 */
}

.slowpoke-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
}

.slowpoke-spinner img {
  width: 180px; /* 이미지 크기 */
  height: 180px;
  animation: spin 2s linear infinite; /* 회전 애니메이션 */
}

/* 회전 애니메이션 */
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}


</style>
