<template>
  <!-- Main Section -->
  <main class="main">
    <div class="main-content">
      <!-- 헤드라인 섹션 -->
      <div class="headline">
        <h1 class="headline-title">🎵 당신이 좋아하는 멜로디, 당신을 위한 영화 이야기 🎬</h1>
        <p class="headline-subtitle">
          <span class="highlight">BeatMovieWelcome</span>은 당신의 음악 취향을 기반으로 마음에 꼭 맞는 영화를 추천합니다.
        </p>
        <p class="headline-subtitle">
          지금, 당신만을 위한 특별한 영화 여행을 시작하세요.
        </p>
      </div>

      <!-- 버튼 섹션 -->
      <div class="buttons">
        <button class="btn btn-info" @click="openRecommendationModal">AI 추천</button>
        <button class="btn btn-reserve" @click="scrollToSection('music')">Music / Movie Top 10</button>
        <!-- <button class="btn btn-reserve" @click="scrollToSection('movie')">Movie Top 10</button> -->
      </div>
    </div>
  </main>

  <!-- 노래 Top 10 섹션 -->
   <div class="body">

  
  <div ref="musicSection">
    <h2 class="subtitle-music">Music Top 10</h2>
  </div>
  <div class="carousel-container ">
    <button class="arrow left" @click="scrollLeft1">‹</button>
    <div class="carousel">
      <MusicPopularList
        v-for="(music, index) in visibleMusics"
        :key="index"
        :music="music"
      />
    </div>
    <button class="arrow right" @click="scrollRight1">›</button>
  </div>

  <!-- 영화 Top 10 섹션 -->
  <div ref="movieSection">
    <h2 class="subtitle-movie">Movie Top 10</h2>
  </div>
  <div class="carousel-container">
    <button class="arrow left" @click="scrollLeft">‹</button>
    <div class="carousel">
      <MoviePopularList
        v-for="(movie, index) in visibleMovies"
        :key="index"
        :movie="movie"
        :index="store.movies.indexOf(movie)"
      />
    </div>
    <button class="arrow right" @click="scrollRight">›</button>
  </div>

  <!-- MovieRecommend 모달 -->
  <MovieRecommendModal 
    v-if="isModalVisible"
    @close="closeRecommendationModal"
  />
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie.js'
import { useMusicStore } from '@/stores/music'
import { onMounted, ref, computed } from 'vue'
import MoviePopularList from '@/components/Movie/MoviePopularList.vue'
import MusicPopularList from '@/components/Music/MusicPopularList.vue'
import MovieRecommendModal from '@/components/Movie/MovieRecommend/MovieRecommendModal.vue'

// 스토어 및 상태 관리
const store = useMovieStore()
const musicStore = useMusicStore()
const currentIndex = ref(0)
const currentIndex1 = ref(0)
const isModalVisible = ref(false)

// 참조를 위한 ref
const musicSection = ref(null)
const movieSection = ref(null)

// 모달 열기 및 닫기
const openRecommendationModal = () => {
  isModalVisible.value = true
}
const closeRecommendationModal = () => {
  isModalVisible.value = false
  
}


// 스크롤 이동 (Navbar와 겹치지 않도록 offset 추가)
const scrollToSection = (section) => {
  let target;
  if (section === 'music') {
    target = musicSection.value;
  } else if (section === 'movie') {
    target = movieSection.value;
  }

  if (target) {
    const navbarHeight = 60; // Navbar 높이
    const offset = target.offsetTop - navbarHeight; // Navbar 높이만큼 보정
    window.scrollTo({
      top: offset,
      behavior: 'smooth',
    });
  }
}

// 인기 영화 및 노래 데이터
onMounted(() => {
  currentIndex.value = Math.floor(store.movies.length / 2) + 4;
  currentIndex1.value = Math.floor(musicStore.musics.length / 2) + 3
  store.getPopularMovie()
  musicStore.getPopularMusic()
})

// 현재 보이는 영화 Top 10
const visibleMovies = computed(() => {
  if (store.movies.length === 0) return []
  const moviesCount = store.movies.length
  return Array.from({ length: 10 }, (_, i) => store.movies[(currentIndex.value + i) % moviesCount])
})

// 현재 보이는 노래 Top 10
const visibleMusics = computed(() => {
  if (musicStore.musics.length === 0) return []
  const musicsCount = musicStore.musics.length
  return Array.from({ length: 10 }, (_, i) => musicStore.musics[(currentIndex1.value + i) % musicsCount])
})



// 캐러셀 이동
// 영화 캐러셀
const scrollLeft = () => {
  const moviesCount = store.movies.length
  currentIndex.value = (currentIndex.value - 1 + moviesCount) % moviesCount
}
const scrollRight = () => {
  const moviesCount = store.movies.length
  currentIndex.value = (currentIndex.value + 1) % moviesCount
}

// 음악 캐러셀
const scrollLeft1 = () => {
  const musicsCount = musicStore.musics.length
  currentIndex1.value = (currentIndex1.value - 1 + musicsCount) % musicsCount
}
const scrollRight1 = () => {
  const musicsCount = musicStore.musics.length
  currentIndex1.value = (currentIndex1.value + 1) % musicsCount
}
</script>

<style scoped>
/* 전체 배경색 지정 */
.body {
  background-color: #151314; /* 배경색을 부모 영역 전체에 적용 */
  color: #ffffff;
  margin: 0;
  padding: 0;
  min-height: 100vh; /* 화면 전체 높이를 채워 빈 공간 방지 */
  overflow-x: hidden; /* 가로 스크롤 방지 */
}

/* 메인 스타일 */
.main {
  margin-top: 60px;
  position: relative;
  height: calc(100vh - 60px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background-color: #151314;
  background-image: url('../../assets/main_image.jpg');
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  user-select: none;
}

/* 헤드라인 스타일 */
.headline {
  margin-bottom: 30px;
  text-align: center;
  color: #ffffff;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
  user-select: none;
}

.headline-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.headline-subtitle {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 15px;
}

/* 강조 텍스트 */
.highlight {
  font-size: 2rem;
  font-weight: bold;
  background: linear-gradient(45deg, #ff4d4d, #ffae00, #00d4ff, #8a2be2);
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  animation: glow 3s infinite;
  text-shadow: 1px 1px 0.5px rgba(0, 0, 0, 0.3);
}
/* 노래 Top 10 제목 스타일 */
.subtitle-music {
  user-select: none;
  font-size: 3rem;
  font-weight: bold;
  text-align: center;
  margin: 30px 0;
  background: linear-gradient(90deg, #ff7eb3, #ff758c, #ff6c4f, #ffae34); /* 핑크-주황 계열 */
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent; /* 텍스트 색상을 투명으로 설정 (그라데이션 표시) */
  text-shadow: 0px 4px 10px rgba(255, 174, 52, 0.6), 
               0px 2px 5px rgba(255, 174, 52, 0.4); /* 글로우 효과 */
  animation: subtitle-glow-music 3s infinite alternate; /* 애니메이션 추가 */
}

/* 영화 Top 10 제목 스타일 */
.subtitle-movie {
  user-select: none;
  font-size: 3rem;
  font-weight: bold;
  text-align: center;
  margin: 30px 0;

  background: linear-gradient(90deg, #7eb3ff, #758cff, #6c4fff, #ae34ff); /* 파란색-보라색 계열 */
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent; /* 텍스트 색상을 투명으로 설정 */
  text-shadow: 0px 4px 10px rgba(174, 52, 255, 0.6), 
               0px 2px 5px rgba(174, 52, 255, 0.4); /* 글로우 효과 */
  animation: subtitle-glow-movie 3s infinite alternate; /* 애니메이션 추가 */
}

/* 노래 제목 애니메이션 */
@keyframes subtitle-glow-music {
  0% {
    text-shadow: 0px 4px 10px rgba(255, 174, 52, 0.6),
                 0px 2px 5px rgba(255, 174, 52, 0.4);
  }
  50% {
    text-shadow: 0px 6px 15px rgba(255, 255, 255, 0.8),
                 0px 3px 8px rgba(255, 174, 52, 0.7);
  }
  100% {
    text-shadow: 0px 4px 10px rgba(255, 174, 52, 0.6),
                 0px 2px 5px rgba(255, 174, 52, 0.4);
  }
}

/* 영화 제목 애니메이션 */
@keyframes subtitle-glow-movie {
  0% {
    text-shadow: 0px 4px 10px rgba(174, 52, 255, 0.6),
                 0px 2px 5px rgba(174, 52, 255, 0.4);
  }
  50% {
    text-shadow: 0px 6px 15px rgba(255, 255, 255, 0.8),
                 0px 3px 8px rgba(174, 52, 255, 0.7);
  }
  100% {
    text-shadow: 0px 4px 10px rgba(174, 52, 255, 0.6),
                 0px 2px 5px rgba(174, 52, 255, 0.4);
  }
}

@keyframes glow {
  0% {
    text-shadow: 0 0 10px #ff4d4d, 0 0 20px #ffae00, 0 0 30px #00d4ff, 0 0 40px #8a2be2;
  }
  50% {
    text-shadow: 0 0 20px #ff4d4d, 0 0 30px #ffae00, 0 0 40px #00d4ff, 0 0 50px #8a2be2;
  }
  100% {
    text-shadow: 0 0 10px #ff4d4d, 0 0 20px #ffae00, 0 0 30px #00d4ff, 0 0 40px #8a2be2;
  }
}

/* 버튼 스타일 */
.buttons {
  user-select: none;
  display: flex;
  gap: 15px;
  justify-content: center;
  
}

.btn {
  padding: 12px 25px;
  font-size: 1.1rem;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-info {
  background-color: #0066ff;
  color: #fff;
}
.btn-reserve {
  background-color: #444;
  color: #fff;
}


/* 캐러셀 */
.carousel-container {
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden;
  
}

.carousel {
  display: flex;
  gap: 12px;
  padding: 70px;
  width: 100%;
  justify-content: center;
  align-items: center;
  transform: translateX(calc(50% - 50vw)); /* 화면 중앙 기준으로 조정 */
  scroll-behavior: smooth; /* 부드러운 스크롤 */
}

/* 캐러셀 포스터 기본 스타일 */
.carousel-container .poster-container {
  position: relative;
  transition: transform 0.3s ease, z-index 0.3s ease; /* 부드러운 효과 */
}

/* 포스터 호버 시 스타일 */
.carousel-container .poster-container:hover {
  z-index: 100; /* 포스터를 가장 앞으로 보이게 설정 */
  transform: scale(1.2); /* 크기를 확대 */
}

.arrow {
  background: rgba(0, 0, 0, 0.6); /* 반투명한 검은 배경 */
  border: none;
  font-size: 3rem; /* 화살표 크기 */
  cursor: pointer;
  color: #fff; /* 화살표 색상 */
  padding: 5px 12px; /* 상자의 크기를 유지하면서 여백 설정 */
  border-radius: 8px; /* 약간의 둥근 모서리 */
  transition: transform 0.2s, background-color 0.2s; /* 부드러운 애니메이션 */
  display: flex; /* 중앙 정렬을 위해 flexbox 사용 */
  align-items: center; /* 세로 중앙 정렬 */
  justify-content: center; /* 가로 중앙 정렬 */
}

.arrow:hover {
  transform: scale(1.3); /* 호버 시 크기 약간 확대 */
  background: rgba(255, 255, 255, 0.3); /* 호버 시 배경색 변경 */
  
}

/* 왼쪽 화살표 위치 */
.left {
  position: absolute;
  left: 15px; /* 여백 조정 */
  z-index: 10;
}

/* 오른쪽 화살표 위치 */
.right {
  position: absolute;
  right: 15px; /* 여백 조정 */
  z-index: 10;
}

</style>
