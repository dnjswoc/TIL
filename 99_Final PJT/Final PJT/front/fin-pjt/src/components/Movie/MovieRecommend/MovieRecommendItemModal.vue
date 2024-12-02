<template>
  <div class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <!-- 닫기 버튼 -->
        <buttonc class="close-button" @click="closeModal" >×</buttonc>

      <!-- 모달 내부 배치 -->
      <div class="modal-body">
        <!-- 포스터 -->
        <div class="poster-container">
          <img :src="posterUrl + recommendStore.movieDetail.poster_path" alt="poster" class="poster-img" />
        </div>

        <!-- 영화 정보 -->
        <div class="movie-details">
          <h2>{{ recommendStore.movieDetail.title }}</h2>

          <!-- 좋아요 버튼 -->
          <div class="like-button-container">
              <button @click="toggleLike" class="like-button">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    :fill="likeUsers.indexOf(userId) > -1 ? 'red' : 'none'" 
                    stroke="white" 
                    stroke-width="1"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                  </svg>
              </button>
              <p class="like-count"><strong >{{ likeUsersLength }}명이 이 영화를 좋아합니다.</strong></p>
            </div>
          <hr>
          <p>{{ recommendStore.movieDetail.overview }}</p>
          <hr>
          <p><strong>개봉일:</strong> {{ recommendStore.movieDetail.release_date }}</p>
          <p><strong>상영시간 : </strong>{{ formattedRuntime }}</p>
          <p><strong>장르:</strong> {{ recommendStore.movieDetail.genre1 }} / {{ recommendStore.movieDetail.genre2 }}</p>
          <MovieRecommendItemYoutube />
          
        </div>
      </div>

      <!-- 한줄평 폼 -->
      <div class="comment-section">
        <MovieCommentForm 
        :movieId="recommendStore.movieDetail.movie_id"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, computed, ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { useRecommendStore } from '@/stores/recommend';
import { useAccountStore } from '@/stores/account';
import MovieGenrePopularItemYoutube from '@/components/Movie/MovieGenrePopularItemYoutube.vue';
import MovieRecommendItemYoutube from './MovieRecommendItemYoutube.vue';
import MovieCommentForm from '@/components/Movie/MovieComment/MovieCommentForm.vue';
import axios from 'axios';

// store 관리
const store = useMovieStore();
const recommendStore = useRecommendStore()
const accountStore = useAccountStore()

// django 기본 url
const posterUrl = store.posterUrl;


const isLiked = ref((recommendStore.movieDetail.like_users.indexOf(accountStore.userId.id)) > 0 ? true : false)

// 좋아요 버튼 작동
const toggleLike = () => {
  isLiked.value = !isLiked.value;
  likeMovie(recommendStore.movieDetail.movie_id);
};

const userId = accountStore.userId.id


// 좋아요 로직
const likeMovie = function (id) {
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/movies/${id}/likes/`,
    headers : {
      Authorization: `Token ${accountStore.token}`,
    }
  })
  .then((res) => {
    console.log(res.data)
    // console.log('좋아요!')
    // like_message.value = res.data.message
    recommendStore.getMovieDetails(recommendStore.movieDetail.movie_id)
  })
  .catch((err) => {
    console.log(err)
  })
}

// 좋아요 수
const likeUsersLength = computed(() => {
  return recommendStore.movieDetail.like_users.length
})

// 좋아요한 유저 id
const likeUsers = computed(() => {
  return recommendStore.movieDetail.like_users
})


// 상영시간을 "시간과 분" 형식으로 변환
const formattedRuntime = computed(() => {
  const runtime = recommendStore.movieDetail.runtime; // 상영시간(분)
  if (!runtime) return "정보 없음"; // runtime이 없을 경우
  const hours = Math.floor(runtime / 60); // 시간 계산
  const minutes = runtime % 60; // 나머지 분 계산
  return `${hours}시간 ${minutes}분`; // 형식화된 문자열 반환
});

const emit = defineEmits();

const closeModal = () => {
  emit('close');  // 모달을 닫는 이벤트를 부모에게 전달
};
</script>

<style scoped>
/* 좋아요 버튼 컨테이너 */
.like-button-container {
  display: flex;
  align-items: center; /* 하트와 텍스트 높이 정렬 */
  gap: 8px; /* 버튼과 텍스트 간격 */
  margin-bottom: 15px; /* 제목과 간격 */
  font-size: 1rem;
  color: #ddd; /* 텍스트 색상 */
}

/* 좋아요 버튼 */
.like-button {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.like-count{
  padding-top: 10px;
}

.like-button svg {
  width: 32px; /* 하트 크기 */
  height: 32px;
  transition: fill 0.3s ease, stroke 0.3s ease;
}

/* 좋아요 상태에 따른 하트 색상 변화 */
.like-button svg:hover {
  stroke: red; /* 호버 시 테두리 빨간색 */
}

.like-button p {
  margin: 0; /* 텍스트 여백 제거 */
  line-height: 1.5; /* 텍스트와 하트 높이 맞춤 */
  font-size: 1.2rem; /* 텍스트 크기 */
  color: #fff; /* 텍스트 색상 */
  align-items: inherit;
}




/* 모달 배경 설정 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9); /* 검은색 배경에 약간 불투명 */
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
}

/* 모달 내부 배치 */
.modal-body {
  display: flex; /* 포스터와 영화 정보 가로 배치 */
  gap: 20px;
  padding: 20px;
}

/* 포스터 컨테이너 */
.poster-container {
  flex: 1; /* 포스터 공간 */
  display: flex;
  justify-content: center; /* 가운데 정렬 */
  align-items: center; /* 수직 가운데 정렬 */
  padding: 20px; /* 여백 추가 */
}

/* 포스터 이미지 */
.poster-img {
  width: 100%;
  max-width: 500px; /* 포스터 최대 크기 */
  height: auto; /* 비율 유지 */
  border-radius: 12px; /* 부드러운 모서리 */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5); /* 부드러운 그림자 */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* 마우스 오버 효과 */
}

/* 포스터 이미지 마우스 오버 */
.poster-img:hover {
  transform: scale(1.05); /* 살짝 확대 */
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.7); /* 그림자 강화 */
}

/* 영화 정보 */
.movie-details {
  flex: 3; /* 영화 정보 공간 */
  color: #f5f5f5; /* 흰색 텍스트 */
}

/* 영화 제목 스타일 */
.movie-details h2 {
  margin-top: 0;
  font-size: 2rem; /* 제목 크기 */
  font-weight: bold;
  color: #ffd700; /* 고급스러운 골드 톤 */
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8); /* 텍스트 그림자 */
}
.movie-details p {
  font-size: 1rem; /* 기본 텍스트 크기 */
  line-height: 1.6; /* 텍스트 줄 간격 */
  margin-bottom: 10px;
  color: #ddd; /* 회색 텍스트 */
}

.movie-details strong {
  color: #fff; /* 강조 텍스트 색상 */
}

/* 한줄평 섹션 */
.comment-section {
  padding: 20px;
  border-top: 1px solid #444; /* 위와 구분선 */
}

.comment-section form {
  display: flex;
  flex-direction: column; /* 한줄평 입력 필드와 버튼을 세로 배치 */
}

.comment-section input[type="text"] {
  padding: 12px;
  border: 1px solid #444; /* 입력 필드 테두리 */
  border-radius: 8px;
  margin-bottom: 12px;
  font-size: 16px;
  color: #fff; /* 텍스트 색상 */
  background: #333; /* 어두운 배경 */
}

.comment-section input[type="text"]::placeholder {
  color: #aaa; /* 플레이스홀더 색상 */
}

.comment-section input[type="submit"] {
  padding: 12px;
  background: #e50914; /* 빨간색 버튼 */
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s ease;
}

.comment-section input[type="submit"]:hover {
  background: #b00710; /* 어두운 빨간색 */
}

/* 닫기 버튼 */
.close-button {
  position: absolute; /* 모달 내부에서 절대 위치 */
  top: 17px; /* 위쪽에서 15px 떨어짐 */
  right: 20px; /* 오른쪽에서 15px 떨어짐 */
  background: none; /* 배경 제거 */
  border: none; /* 테두리 제거 */
  font-size: 35px; /* 버튼 크기 */
  font-weight: bold; /* 두꺼운 글꼴 */
  cursor: pointer; /* 클릭 가능한 커서 */
  color: #f5f5f5; /* 흰색 */
  transition: color 0.3s ease; /* 마우스 오버 시 부드러운 색상 변화 */
  z-index: 1000; /* 최상단에 위치 */
}

.close-button:hover {
  color: #ff0000; /* 마우스 오버 시 빨간색 */
}

/* 스크롤바 스타일 */
.modal-content::-webkit-scrollbar {
  width: 8px;
}

.modal-content::-webkit-scrollbar-thumb {
  background: #444; /* 스크롤바 색상 */
  border-radius: 4px;
}

.modal-content::-webkit-scrollbar-thumb:hover {
  background: #666; /* 스크롤바 호버 색상 */
}

.modal-content::-webkit-scrollbar-track {
  background: #222; /* 스크롤바 배경 */
}
</style>
