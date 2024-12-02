import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router/dist/vue-router'
import { useAccountStore } from '@/stores/account'

export const useCommunityStore = defineStore('community', () => {
  const freearticles = ref([])   // 자유게시글 목록
  const comments = ref([])  // 댓글 목록
  const API_URL = 'http://127.0.0.1:8000'

  const userStore = useAccountStore()
  const token = userStore.token

  // 자유게시판 게시글 조회
  const getfreeArticles = function () {
    axios({
      method : 'get',
      url : `${API_URL}/articles/free_article_list/`
    })
    .then(response => {
      console.log(response.data)
      freearticles.value = response.data
    })
    .catch(error => {
      console.log(error)
    })
  }

  // 영화게시판 게시글 조회
  const getMovieArticles = function () {
    axios({
      method : 'get',
      url : `${API_URL}/articles/movie_article_list/`
    })
    .then(response => {
      console.log(response.data)

    })
    .catch(error => {
      console.log(error)
    })
  }

  // 자유게시판 댓글 목록 조회 함수
  const getFreeArticleComments = function (freeArticleId) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/free_article/${freeArticleId}/comments/`
      })
        .then(response => {
          comments.value = response.data
          console.log(comments.value)
        })
        .catch(error => {
          console.error('댓글 조회 실패:', error)
        })
    }

  // 댓글 생성 함수
  const addFreeArticleComment = function (freeArticleId, content) {
    axios({
      method : 'post',
      url : `${API_URL}/articles/free_article/${freeArticleId}/comments/`,
      data : {content:content},
      headers : {Authorization : `Token ${token}`}
    })
    .then((res) => {
      comments.value.push(res.data)
      getFreeArticleComments(freeArticleId)
      console.log('댓글 생성 성공,' , res.data)
    })
    .catch((error) => {
      console.log('댓글 생성 실패 : ',  error)
    })
  }

  // 댓글 수정 함수
  const updateFreeArticleComment = function (freeArticleId, commentId, updatedContent) {
  axios({
    method: 'put',
    url: `${API_URL}/articles/free_article/${freeArticleId}/comments/${commentId}/`,
    data: { content: updatedContent },
    headers: {
      Authorization: `Token ${token}`,
    },
  })
    .then(response => {
      console.log('댓글 수정 성공:', response.data);
      // 수정된 댓글 정보를 로컬에서 갱신
      const commentIndex = comments.value.findIndex(comment => comment.id === commentId);
      if (commentIndex !== -1) {
        comments.value[commentIndex].content = response.data.content;
      }
    })
    .catch(error => {
      console.error('댓글 수정 실패:', error);
    });
};



  // 자유게시글 댓글 삭제 함수
  const deleteFreeArticleComment = function (freeArticleId, commentId) {
    axios({
      method: 'delete',
      url: `${API_URL}/articles/free_article/${freeArticleId}/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then(() => {
        console.log('댓글 삭제 성공');
        // 댓글 삭제 후, 로컬에서 해당 댓글을 삭제
        getFreeArticleComments(freeArticleId)  // 삭제 후 댓글 목록 다시 가져오기
      })
      .catch(error => {
        console.error('댓글 삭제 실패:', error)
      })
  }

  // 자유게시판 댓글 갯수 세기
  const freeArticleCommentCount = computed(() => {
    return comments.value.length
  })

  return  { 
    comments,
    freearticles, 
    API_URL, 
    getfreeArticles, 
    deleteFreeArticleComment, 
    getFreeArticleComments , 
    addFreeArticleComment, 
    updateFreeArticleComment,
    freeArticleCommentCount,
    getMovieArticles
  }
}, { persist: true })