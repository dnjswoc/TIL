<template>

  <div class="login-wrapper">
    <div class="login-container">
    
        <h1 class="mb-4 text-center">LOGIN</h1>
        <div class="email-login">
        <form @submit.prevent="logIn">
          <div class="mb-3">
            <label for="username" class="form-label">아이디</label>
            <input type="text" class="form-control" id="username" v-model.trim="username" placeholder="ID를 입력해주세요." @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">비밀번호</label>
            <input type="password" class="form-control" id="password" v-model.trim="password" placeholder="비밀번호를 입력해주세요." @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}">
          </div>
          <button type="submit" class="login-button">로그인</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const username = ref(null)
const password = ref(null)

const store = useAccountStore()

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 


.login-wrapper {
  user-select: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Montserrat', sans-serif;
  height: 110vh;
  background-color: #121212;
}

.login-container {
  background-color: #1e1e1e;
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  color: #ffffff;
  width: 460px;
  padding: 3rem;
  text-align: center;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  border: 1px solid #333;
}

.email-login {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.email-login input {
  padding: 0.75rem 1rem;
  border-radius: 24px;
  border: 1px solid #444;
  background-color: #222;
  color: #fff;
  opacity: 0.8;
  transition: all 0.3s ease-in-out;
}

.email-login input.expanded-input {
  padding: 0.75rem 1.5rem;
  width: 100%;
}

.email-login input::placeholder {
  color: #b3b3b3;
}

.email-login input:hover{
  border-color: #1db954;
  opacity: 1;
}

.login-button {
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  background-color: #1db954;
  color: #fff;
  border: none;
  width: 100%;
  padding: 0.75rem 1.5rem;
  margin-top:15px;
  border-radius: 24px;
  font-size: 1rem;
  cursor: pointer;
}


</style>
