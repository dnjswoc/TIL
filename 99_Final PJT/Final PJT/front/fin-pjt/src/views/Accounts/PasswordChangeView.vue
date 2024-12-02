<template>
  <div class="password-change-wrapper">
    <div class="password-change-container">
      <h1 class="mb-4 text-center">비밀번호 변경</h1>
      <div class="password-change-form">
        <form @submit.prevent="passwordChange">
          <div class="mb-3">
            <label for="new_password1" class="form-label">새 비밀번호</label>
            <input type="password" class="form-control" id="new_password1" v-model.trim="new_password1" placeholder="새 비밀번호를 입력해주세요." required @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}">
          </div>
          <div class="mb-3">
            <label for="new_password2" class="form-label">비밀번호 확인</label>
            <input type="password" class="form-control" id="new_password2" v-model.trim="new_password2" placeholder="새 비밀번호를 다시 입력해주세요." required @focus="inputFocus = true" @blur="inputFocus = false" :class="{'expanded-input focused': inputFocus}">
          </div>
          <button type="submit" class="password-change-button">비밀번호 변경하기</button>
        </form>
        <form @submit.prevent="goToUpdate">
          <button type="submit" class="cancel-button">취소</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'
import { useRouter } from 'vue-router';


// 스토어, 라우터 설정
const store = useAccountStore()
const router = useRouter()

// 반응형 변수 선언
const new_password1 = ref(null)
const new_password2 = ref(null)



// 비밂번호 변경
const passwordChange = () => {
  const payload = {
    new_password1: new_password1.value,
    new_password2: new_password2.value,
  }
  store.passwordChange(payload)
}

// 비밀번호 변경 취소 시 회원정보 수정으로 돌아가기
const goToUpdate = function () {
  console.log('비밀번호 변경 취소')
  router.push({ name: 'profileUpdate'})
}

</script>

<style scoped>
.password-change-wrapper {
  user-select: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Montserrat', sans-serif;
  height: 110vh;
  background-color: #121212;
}

.password-change-container {
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

.password-change-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.password-change-form input {
  padding: 0.75rem 1rem;
  border-radius: 24px;
  border: 1px solid #444;
  background-color: #222;
  color: #fff;
  opacity: 0.8;
  transition: all 0.3s ease-in-out;
}

.password-change-form input.expanded-input {
  padding: 0.75rem 1.5rem;
  width: 100%;
}

.password-change-form input::placeholder {
  color: #b3b3b3;
}

.password-change-form input:hover
{
  border-color: #1db954;
  opacity: 1;
}



.password-change-button {
  background-color: #1db954;
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  color: #fff;
  border: none;
  width:100%;
  padding: 0.75rem 1.5rem;
  margin-top: 15px;
  border-radius: 24px;
  font-size: 1rem;
  cursor: pointer;
}


.cancel-button {
  background-color: #6e6e6e;
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  color: #fff;
  border: none;
  width: 100%;
  padding: 0.75rem 1.5rem;
  border-radius: 24px;
  font-size: 1rem;
  cursor: pointer;
}

</style>