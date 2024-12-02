<template>
  <div class="body">

 
  <div class="signup-wrapper">
    <div class="signup-container">
      <h1 class="mb-4 text-center">SIGN UP</h1>
      <p class="info-text">※ 필수 입력사항은 반드시 입력해주세요.</p>
      <div class="email-signup">
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label required-label">아이디</label>
          <input type="text" class="form-control required-input" id="username" v-model.trim="username" placeholder="[필수] 아이디를 입력해주세요." required>
        </div>
        <div class="mb-3">
          <label for="password1" class="form-label required-label">비밀번호</label>
          <input type="password" class="form-control required-input" id="password1" v-model.trim="password1" placeholder="[필수] 비밀번호를 입력해주세요." required>
        </div>
        <div class="mb-3">
          <label for="password2" class="form-label required-label">비밀번호 확인</label>
          <input type="password" class="form-control required-input" id="password2" v-model.trim="password2" placeholder="[필수] 비밀번호를 다시 입력해주세요." required>
        </div>
        <div class="mb-3">
          <label for="nickname" class="form-label required-label">닉네임</label>
          <input type="text" class="form-control required-input" id="nickname" v-model.trim="nickname" placeholder="[필수] 닉네임을 입력해주세요." required>
        </div>
        <div class="mb-3">
          <label for="genre1" class="form-label">선호하는 노래 장르 1</label>
          <input type="text" class="form-control" id="genre1" v-model.trim="genre1" placeholder="ex. [선택] Pop, Jazz, Dance, 발라드, 힙합">
        </div>
        <div class="mb-3">
          <label for="genre2" class="form-label">선호하는 노래 장르 2</label>
          <input type="text" class="form-control" id="genre2" v-model.trim="genre2" placeholder="[선택] 하나 더 적을 수 있어요.">
        </div>
        <div class="mb-3">
          <label for="introduction" class="form-label">소개글</label>
          <textarea class="form-control" id="introduction" v-model.trim="introduction" rows="3" placeholder="[선택] 본인을 소개하는 글을 작성해주세요."></textarea>
        </div>
        <button type="submit" class="signup-button">회원가입</button>
      </form>
    </div>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

// 회원가입 시 입력할 필드들
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref('')
const genre1 = ref('')
const genre2 = ref('')
const introduction = ref('')

const store = useAccountStore()

// 양방향 바인딩을 통해 회원가입 시 입력값 넘겨주기
const signUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    genre1: genre1.value,
    genre2: genre2.value,
    introduction: introduction.value,
  }
  store.signUp(payload)
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


.signup-wrapper {
  user-select: none;
  padding-top: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Montserrat', sans-serif;
  height: 190vh;
  background-color: #151314;
}

.signup-container {
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  background-color: #1e1e1e;
  color: #ffffff;
  width: 460px;
  padding: 2rem;
  text-align: center;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  border: 1px solid #333;
}

.email-signup {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.email-signup input {
  font-family: 'Arial', sans-serif;
  padding: 0.75rem 1rem;
  border-radius: 24px;
  border: 1px solid #444;
  background-color: #222;
  color: #fff;
  opacity: 0.8;
}

.email-signup textarea {
  padding: 0.75rem 1rem;
  border-radius: 24px;
  border: 1px solid #444;
  background-color: #222;
  color: #fff;
  opacity: 0.8;
  transition: all 0.3s ease-in-out;
}

.email-signup input:hover,
.email-signup textarea:hover {
  border-color: #1db954;
  opacity: 1;
}

.email-signup input::placeholder {
  color: #b3b3b3;
}

.email-signup textarea::placeholder {
  color: #b3b3b3;
}

.required-label {
  color: #ffa500; /* 오렌지 색상으로 필수 입력 강조 */
}

.required-input {
  border: 2px solid #ffa500;
}

.signup-button {
  user-select: none;
  font-weight: bold;
  background-color: #1db954;
  color: #fff;
  border: none;
  width: 100%;
  padding: 0.75rem 1.5rem;
  margin-top: 15px;
  border-radius: 24px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.signup-button:hover {
  background-color: #17a441;
}
</style>
