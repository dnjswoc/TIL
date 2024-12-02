<template>
  <div>
    <div class="update-wrapper">
    <div class="update-container">
      <h1 class="mb-4 text-center">MODIFYING INFO</h1>
      <p class="info-text">※ 필수 입력사항은 반드시 입력해주세요.</p>
      <div class="update-form">
        <form @submit.prevent="profileUpdate">
          <div class="mb-3">
            <label for="nickname" class="form-label required-label">닉네임</label>
            <input type="text" class="form-control" id="nickname" v-model.trim="nickname" placeholder="[필수] 닉네임을 입력해주세요" @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}">
          </div>
          <div class="mb-3">
            <label for="genre1" class="form-label">노래 장르 1</label>
            <input type="text" class="form-control" id="genre1" v-model.trim="genre1" placeholder="[선택] 좋아하는 노래 장르를 선택해주세요" @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}">
          </div>
          <div class="mb-3">
            <label for="genre2" class="form-label">노래 장르 2</label>
            <input type="text" class="form-control" id="genre2" v-model.trim="genre2" placeholder="[선택] 좋아하는 노래 장르를 선택해주세요." @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}">
          </div>
          <div class="mb-3">
            <label for="introduction" class="form-label">소개글</label>
            <textarea class="form-control" id="introduction" v-model.trim="introduction" rows="3" placeholder="[선택] 본인을 소개하는 글을 써주세요" @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}"></textarea>
          </div>

          <button type="submit" class="update-button">수정</button>
        </form>
        <form @submit.prevent="goToPasswordChange">
          <button type="submit" class="password-change-button">비밀번호 변경</button>
        </form>
        <form @submit.prevent="goToProfile">
          <button type="submit" class="cancel-button">취소</button>
        </form>

      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import { useRouter } from 'vue-router';

// const props = defineProps({
//   id : Number
// })


const store = useAccountStore()
const router = useRouter()

const userId = store.userInfo

// 기존 회원정보를 기반으로 수정할 수 있게 값을 저장해놓고 시작
// const { nickname, genre1, genre2, introduction } = userId

const nickname = ref(userId.nickname)
const genre1 = ref(userId.genre1)
const genre2 = ref(userId.genre2)
const introduction = ref(userId.introduction)
const id = userId.id



// const nickname = userId.nickname

// 회원정보 수정 함수
const profileUpdate = () => {
  const payload = {
    nickname: nickname.value,
    genre1: genre1.value,
    genre2: genre2.value,
    introduction: introduction.value,
  }
  console.log(payload)
  store.profileUpdate(payload)
}

// 회원정보 수정 취소 시 프로필로 돌아가기
const goToProfile = function () {
  console.log('회원정보 수정 취소')
  router.push({ name: 'profile'})
}

// 비밀번호 변경 페이지로 이동
const goToPasswordChange = function () {
  console.log('비밀번호 변경 페이지 이동')
  router.push({ name: 'profilePasswordChange' })
}



</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

.info-text {
  font-size: 0.8rem;
  color: #ffa500;
  text-align: center;
  margin-bottom: 10px;
  opacity: 0.9;
}

.required-label {
  color: #ffa500; /* 오렌지 색상으로 필수 입력 강조 */
}


.update-wrapper {
  user-select: none;
  font-family: 'Arial', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Montserrat', sans-serif;
  height: 120vh;  /* 배경 제외 높이 정하기 */
  background-color: #121212;
  /* padding-top:100px; */
}

.update-container {
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  background-color: #1e1e1e;
  color: #ffffff;
  width: 460px;
  padding: 3rem;
  text-align: center;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  border: 1px solid #333;
  
}

.update-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.update-form input {
  padding: 0.75rem 1rem;
  border-radius: 24px;
  border: 1px solid #444;
  background-color: #222;
  color: #fff;
  opacity: 0.8;
  transition: all 0.3s ease-in-out;
}

.update-form textarea {
  padding: 0.75rem 1rem;
  border-radius: 24px;
  border: 1px solid #444;
  background-color: #222;
  color: #fff;
  opacity: 0.8;
  transition: all 0.3s ease-in-out;
}

.update-form input.expanded-input {
  padding: 0.75rem 1.5rem;
  width: 100%;
}

.update-form textarea.expanded-input {
  padding: 0.75rem 1.5rem;
  width: 100%;
}

.update-form input::placeholder {
  color: #b3b3b3;
}

.update-form textarea::placeholder {
  color: #b3b3b3;
}

.update-form input:hover,
.update-form textarea:hover
{
  border-color: #1db954;
  opacity: 1;
}

.update-button {
  background-color: #1db954;
  color: #fff;
  border: none;
  width: 100%;
  padding: 0.75rem 1.5rem;
  border-radius: 24px;
  font-size: 1rem;
  cursor: pointer;
}


.cancel-button {
  background-color: #6e6e6e;
  color: #fff;
  border: none;
  width: 100%;
  padding: 0.75rem 1.5rem;
  border-radius: 24px;
  font-size: 1rem;
  cursor: pointer;
}

.password-change-button {
  background-color: #4d6dd3;
  color: #fff;
  border: none;
  width: 100%;
  padding: 0.75rem 1.5rem;
  border-radius: 24px;
  font-size: 1rem;
  cursor: pointer;
}

</style>