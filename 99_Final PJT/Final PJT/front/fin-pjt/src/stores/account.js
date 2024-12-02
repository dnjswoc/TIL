import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router/dist/vue-router'


export const useAccountStore = defineStore('account', () => {
  
  // django 기본 url
  const API_URL = 'http://127.0.0.1:8000'

  const router = useRouter()

  // 프로필 페이지를 렌더링할 때 사용하는 유저 정보
  const userInfo = ref(null)

  // 팔로우, 언팔로우 버튼에 번갈아 사용할 값
  const followMessage = ref(null)

  // 유저의 모든 정보 담겨있음
  const userId = ref(null)


  // 로그인 시 발급받는 token을 저장할 변수
  const token = ref(null)

  // 로그인한 사람과 작성자 비교 하는 함수
  const isOwner = (id) => {
    return id === userId.value.id
  }



  // 회원가입 함수
  const signUp = function (payload) {
    const { username, password1, password2, nickname, genre1, genre2, introduction } = payload

    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/registration/`,
      data: {
        username, password1, password2, nickname, genre1, genre2, introduction
      }
    })
      .then((res) => {
        console.log(res)
        console.log('회원가입!')
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  // 로그인 함수
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 완료')
        console.log(res)
        token.value = res.data.key
        console.log(token)
        getUserId()
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // user_id 얻는 함수
  const getUserId = function () {
    axios({
      method : 'get',
      url : `${API_URL}/accounts/get_user_id/`,
      headers : {
        Authorization : `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(res.data)
        userId.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 로그아웃 함수
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/logout/`,
    })
      .then((res) => {
        console.log('로그아웃')
        console.log(res)
        token.value = null
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 회원정보 수정 함수
  const profileUpdate = function (payload) {
    const { nickname, genre1, genre2, introduction } = payload
    
    axios({
      method : 'patch',
      url : `${API_URL}/dj-rest-auth/user/`,
      data: {
        nickname, genre1, genre2, introduction
      },
      headers : {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log('회원정보 수정 완료')
        // console.log(res)
        userInfo.value = res.data
        router.push({ name: 'profile'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 비밀번호 변경 함수
  const passwordChange = function (payload) {
    const { new_password1, new_password2 } = payload

    axios({
      method : 'post',
      url : `${API_URL}/dj-rest-auth/password/change/`,
      data : {
        new_password1, new_password2
      },
      headers : {
        Authorization : `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log('비밀번호 변경 완료')
        router.push({ name: 'profile', params : { 'id' : userId.value.id } })
      })
      .catch((err) => {
        console.log(err)
        alert("비밀번호가 일치하지 않습니다!")
      })
  }


  // 프로필 페이지 렌더링 함수
  const getProfile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/${userId.value.id}/`
    })
      .then((res) => {
        console.log(res.data)
        userInfo.value = res.data

      })
      .catch((err) => {
        console.log(err)
      })  
  }
  

  // perplexity, follow 적용 함수
  const follow = function (userId) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/${userId}/follow/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      console.log('팔로우 상태 변경 완료')
      console.log(res.data.message)
      followMessage.value = res.data.message
      getProfile()
    })
    .catch((err) => {
      console.log(err)
    })
  }

  return { 
    signUp,
    logIn, 
    logOut, 
    token, 
    getProfile, 
    userInfo, 
    follow, 
    API_URL, 
    followMessage, 
    profileUpdate, 
    userId, 
    getUserId,
    isOwner,
    passwordChange
   }
}, { persist: true })