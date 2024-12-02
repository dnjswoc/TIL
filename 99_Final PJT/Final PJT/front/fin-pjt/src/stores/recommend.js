import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router/dist/vue-router'
import { useAccountStore } from './account'


export const useRecommendStore = defineStore('recommend', () => {
  
  // django 기본 url
  const API_URL = 'http://127.0.0.1:8000'

  const router = useRouter()

  const accountStore = useAccountStore()

  // 추천받은 영화 목록 저장할 배열
  const movieRecommendList = ref([])

  // 로그인 시 발급받는 토큰
  const token = accountStore.token

  // 단일 영화 디테일 목록을 담을 변수
  const movieDetail = ref(null)

  // 영화 추천 openai api 연결 함수
  const getMovieRecommend = function (genre) {
    axios({
      method : 'get',
      url : `${API_URL}/movies/recommend_movie/${genre}/`,
      headers : {
        Authorization : `Token ${token}`
      }
    })
    .then((res) => {
      console.log(res.data)
      movieRecommendList.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // 영화 아이디 가져오기(openai로 얻어와서 필요X)
  const getMovieId = function (movie_title) {
    axios({
      method : 'get',
      url : `${API_URL}/movies/movie_detail/${movie_title}`,
      header : {
        Authorization : `Token ${token}`
      }
    })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  }


  // 단일 영화 정보 가져오기
  const getMovieDetails = function (movie_id) {
    axios({
      method: 'get',
      url: `${API_URL}/movies/movie_detail/${movie_id}/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((res) => {
        movieDetail.value = res.data
        console.log("Movie detail fetched:", res.data);
        
        return movieDetail
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 영화 예고편 가져오기
  const getMovieTrailers = async function () {
    const youtubeApiKey = import.meta.env.VITE_YOUTUBE_API_KEY; // YouTube API 키
    console.log(movieDetail.value.title)
    console.log(movieDetail.value.release_date)
    const query = `${movieDetail.value.title} 메인 예고편 ${movieDetail.value.release_date.slice(0, 4)}`; // 검색 쿼리

  
    try {
      const response = await axios.get(
        `https://www.googleapis.com/youtube/v3/search`, {
          params: {
            part: 'snippet',
            q: query,
            key: youtubeApiKey,
            type: 'video',
            maxResults: 1,
          }
        }
      );
  
      if (response.data.items && response.data.items.length > 0) {
        const videoId = response.data.items[0].id.videoId;
        return `https://www.youtube.com/embed/${videoId}`; // YouTube 예고편 URL 반환
      } else {
        console.error('예고편을 찾을 수 없습니다.');
        return null;
      }
    } catch (error) {
      console.error('예고편 가져오는 중 오류 발생:', error);
      return null;
    }
  };



  return {
    getMovieRecommend,
    movieRecommendList,
    getMovieId,
    token,
    getMovieDetails,
    getMovieTrailers,
    movieDetail
  }

}, { persist: true })