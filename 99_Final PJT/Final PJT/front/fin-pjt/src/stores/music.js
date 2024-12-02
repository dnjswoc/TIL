import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router/dist/vue-router'
import { useAccountStore } from './account'


export const useMusicStore = defineStore('music', () => {

  // 인기차트 노래 목록 담을 배열
  const musicList = ref(null)

  // 노래 상세 정보
  const musicDetail = ref(null)

  // 로그인 토큰 호출
  const store = useAccountStore()

  let musics = ref([])

  // 인기차트 노래 목록 가져올 함수
  const getPopularMusic = function () {
    axios({
      method : 'get',
      url : 'http://127.0.0.1:8000/musics/music_chart/',
    })
    .then((response) => {
      console.log(response)
      this.musics = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }


  // 단일 노래 정보 가져오기
  const getMusicDetail = function (track_id) {
    axios({
      method : 'get',
      url : `http://127.0.0.1:8000/musics/track_detail/${track_id}/`,
      headers : {
        Authorization : `Token ${store.token}`
      }
    })
    .then((response) => {
      console.log(response.data)
      musicDetail.value = response.data

      return musicDetail
    })
    .catch((error) => {
      console.log(error)
    })
  }


  // 뮤직비디오 가져오기
  const getMusicVideo = async function () {
    const youtubeApiKey = import.meta.env.VITE_YOUTUBE_API_KEY; // YouTube API 키
    const query = `${musicDetail.value.name} ${musicDetail.value.artists[0].name} official 뮤직비디오` // 검색 쿼리

  
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
    musics,
    musicList,
    getPopularMusic,
    getMusicDetail,
    musicDetail,
    getMusicVideo
   }
}, { persist: true })