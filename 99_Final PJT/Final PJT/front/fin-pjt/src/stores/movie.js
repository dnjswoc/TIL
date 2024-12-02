import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAccountStore } from './account'

export const useMovieStore = defineStore('movie', () => {
  const API_KEY = import.meta.env.VITE_TMDB_API_KEY

  const store = useAccountStore()

  // django 기본 서버
  const API_URL = 'http://127.0.0.1:8000'

  // 로그인 시 발급 받는 토큰
  const token = store.token

  // 영화 목록 담을 배열
  const movieList = ref([])

  // 영화 장르를 담을 배열
  const genreList = ref(null)

  // 장르별 영화 목록을 담을 배열
  const movieGenreList = ref([])

  // 단일 영화 디테일 목록을 담을 변수
  const movieDetail = ref(null)

  let movies = ref([])


  // 단일 영화 comments
  const movieComments = ref([])


  // comment초기화
  const newComment = ref({
    content: '',
    rating: 0,
  });

  // 별점 설정
    const setRating = (rating) => {
      newComment.value.rating = rating;
    };
  


  // 포스터 기본 url
  const posterUrl = ref('https://image.tmdb.org/t/p/w200/')

  const getPopularMovie = function () {
    axios({
      url: 'http://127.0.0.1:8000/movies/latest_movie/',
      method : 'GET', 
      headers : {
        Authorization: `Token ${store.token}`
      }
    })
    .then((response) => {
      console.log(response.data)
      this.movies = response.data
    }).catch((error) => {
      console.log(error)
    })
  }

  // 영화 목록 담을 함수
  const getMovieList = function () {
    axios({
      method: 'get',
      url: `${API_URL}/movies/movies_list/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        console.log(res)
        movieList.value = res.data
        movieGenreList.value = []
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 영화 장르 담을 함수
  const getGenreList = function () {
    axios({
      method: 'get',
      url: `${API_URL}/movies/movie_genre_list/`,
    })
      .then((res) => {
        console.log(res.data)
        genreList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 장르별 영화 목록 가져오기
  const getGenreMovieList = function (genre) {
    axios({
      method: 'get',
      url: `${API_URL}/movies/movies_list/${genre}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        console.log(res)
        movieGenreList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 단일 영화 정보 가져오기
  const getMovieDetail = function (movie_id) {
    axios({
      method: 'get',
      url: `${API_URL}/movies/movie_detail/${movie_id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        console.log(res.data)
        movieDetail.value = res.data
        console.log("Movie detail fetched:", res.data);
        
        return movieDetail
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 영화 예고편 가져오기
  const getMovieTrailer = async function () {
    const youtubeApiKey = import.meta.env.VITE_YOUTUBE_API_KEY; // YouTube API 키
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

  // 단일 영화 한줄평 목록 조회
  const getMovieComments = function (movieId) {
    axios({
      method : 'get',
      url : `${API_URL}/movies/movie_comment/${movieId}/`,
      headers: {
        Authorization: `Token ${store.token}`
      },
    })
    .then((response) => {
      
      movieComments.value = response.data
      console.log('한줄평 가져오기 성공 : ', response.data)
    })
    .catch((error) => {
      console.log('영화 한줄평 조회 실패 : ', error)
    })
  }

  // 영화 한줄평 추가 메소드
  const addMovieComment = function (movieId) {
    axios({
      method : 'post',
      url : `${API_URL}/movies/movie_comment/${movieId}/`,
      data : {
        content: newComment.value.content,
        score: newComment.value.rating,
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((res) => {
      console.log('한줄평 저장 성공 : ', res.data)
      movieComments.value.unshift(res.data)
      resetNewComment()  // 댓글 폼 초기화
    })
    .catch((error) => {
      console.log('한줄평 생성 오류 : ', error)
    })
  }

  // 영화 한줄평 삭제 메소드
  const deleteMovieComment = function (movieId, commentId) {
    axios({
      method: 'delete',
      url: `${API_URL}/movies/movie_comment/${movieId}/comment/${commentId}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((response) => {
        console.log('삭제 응답:', response.data);
  
        // 최신 목록 가져오기
        axios({
          method: 'get',
          url: `${API_URL}/movies/movie_comment/${movieId}/`,
          headers: { Authorization: `Token ${store.token}` },
        })
          .then((res) => {
            console.log('최신 댓글 목록:', res.data);
            movieComments.value = res.data;
          })
          .catch((err) => {
            console.error('최신 댓글 목록 요청 실패:', err.response || err);
          });
      })
      .catch((error) => {
        console.error('삭제 실패:', error.response || error);
      });
  };

  // 영화 한줄평 수정 메소드
  const editMovieComment = function (movieId, commentId, updatedComment) {
    axios({
      method: 'put',
      url: `${API_URL}/movies/movie_comment/${movieId}/comment/${commentId}/`,
      data: updatedComment,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((response) => {
        console.log('수정 성공:', response.data);

        // 수정된 데이터로 movieComments 업데이트
        const updatedComments = movieComments.value.map((comment) =>
          comment.id === commentId ? response.data : comment
        );
        movieComments.value = updatedComments;
      })
      .catch((error) => {
        console.error('수정 실패:', error.response || error);
      });
  };

  // 한줄평 초기화
    const resetNewComment = () => {
      newComment.value.content = '';
      newComment.value.rating = 0;
    };
  // 단일영화 한줄평 갯수 세기
  const movieCommentsCount = computed(() => {
    return movieComments.value.length
  })


  return { movies,
          getPopularMovie, 
          getMovieList, 
          movieList, 
          posterUrl,
          movieComments, 
          getGenreMovieList, 
          getMovieDetail, 
          movieDetail, 
          movieGenreList, 
          genreList, 
          getGenreList,
          getMovieTrailer,
          getMovieComments,
          movieCommentsCount,
          resetNewComment,
          addMovieComment,
          setRating,
          newComment,
          resetNewComment,
          deleteMovieComment,
          editMovieComment
        }
}, { persist : true })
