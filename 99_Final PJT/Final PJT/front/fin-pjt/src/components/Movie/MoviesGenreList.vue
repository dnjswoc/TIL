<template>
  <div>
    <h3 class="name">{{ genre.name }}</h3>
    <div class="carousel-container">
    <button class="arrow left" @click="scrollLeft">‹</button>
    <div class="carousel" v-if="movieGenreList">
      <MovieGenrePopularList 
      v-for="(movie, index) in visibleMovies"
        :key="index"
        :movie="movie"
        :index="movieGenreList.indexOf(movie)"
      />
    </div>
    <button class="arrow right" @click="scrollRight">›</button>
  </div>
  </div>
  
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { useAccountStore } from '@/stores/account';
import MovieGenrePopularList from '@/components/Movie/MovieGenrePopularList.vue';
import axios from 'axios';

// 스토어 및 상태 관리
const store = useMovieStore()
const accountStore = useAccountStore()

// 참조를 위한 ref
const movieGenreList = ref(null)
const currentIndex = ref(0) // 현재 시작 포스터의 인덱스

// django 기본 url
const API_URL = store.API_URL

// 로그인 시 받는 token
const token = accountStore.token


// 장르 목록을 반복하며 장르 하나씩 prop된 것을 받아오기
const props = defineProps({
  genre: Object
})

// 현재 보이는 영화
const visibleMovies = computed(() => {
  if (movieGenreList.value.length === 0) return []
  const moviesCount = movieGenreList.value.length
  return Array.from({ length: 10 }, (_, i) => movieGenreList.value[(currentIndex.value + i) % moviesCount])
})


// 캐러셀 이동
const scrollLeft = () => {
  const moviesCount = movieGenreList.value.length
  currentIndex.value = (currentIndex.value - 1 + moviesCount) % moviesCount // 왼쪽으로 이동 시 인덱스 조정
}

const scrollRight = () => {
  const moviesCount = movieGenreList.value.length
  currentIndex.value = (currentIndex.value + 1) % moviesCount // 오른쪽으로 이동 시 인덱스 조정
}



// prop받은 장르별로 인기있는 영화 목록 axios 요청
onMounted(() => {
  
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/movies_list/${props.genre.name}/`,
    headers : {
      Authorization : `Token ${token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      movieGenreList.value = res.data
      currentIndex.value = Math.floor(movieGenreList.value.length / 2) + 4;
    })
    .catch((err) => {
      console.log(err)
    })
    
})

</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

.name{
  font-weight: bold;
  font-family: 'Arial', sans-serif;
  color : gold;
}


.subtitle {
  font-size: 1.5rem; /* 소제목 글자 크기 */
  font-weight: bold;
  margin-bottom: 10px; /* 소제목과 목록 사이의 간격 */
  text-align: center; /* 가운데 정렬 */
}

.carousel-container {
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden; /* 스크롤바 숨기기 */
}

.carousel {
  display: flex;
  gap: 12px;
  padding: 20px;
  width: 100%; /* 부모 요소의 너비를 채움 */
  justify-content: center;
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
  transform: scale(1.3); /* 마우스 올렸을 때 버튼 크기 커지기 */
}
.left {
  position: absolute;
  left: 10px;
  z-index: 10;
}

.right {
  position: absolute;
  right: 10px;
  z-index: 10;
}

</style>