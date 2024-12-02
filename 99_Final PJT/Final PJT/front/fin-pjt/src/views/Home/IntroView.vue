<template>
  <div class="intro-container">
    <h1 class="logo">
      <span class="headphones-icon">
        <i class="fas fa-headphones"></i>
      </span>
      Beat Movie WelCome
      <span class="headphones-icon">
        <i class="fas fa-headphones"></i>
      </span>
    </h1>
    <div class="heartbeat-container">
      <div class="heartbeat short"></div>
      <div class="heartbeat long"></div>
      <div class="heartbeat short"></div>
      <div class="heartbeat long"></div>
      <div class="heartbeat short"></div>
      <div class="heartbeat long"></div>
      <div class="heartbeat short"></div>
      <div class="heartbeat long"></div>
      <div class="heartbeat short"></div>
    </div>
    <button class="welcome-btn" 
            @mouseover="changeText" 
            @mouseleave="resetText" 
            @click="goToHome">
      {{ buttonText }}
    </button>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export default {
  setup() {
    const router = useRouter();
    const buttonText = ref("WelCome!");

    const changeText = () => {
      buttonText.value = "Enjoy!";
    };

    const resetText = () => {
      buttonText.value = "WelCome!";
    };

    const goToHome = () => {
      router.push({ name: 'home' });
    };

    return {
      buttonText,
      changeText,
      resetText,
      goToHome
    };
  }
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 

.intro-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #151314;
  color: #fff;
}

.logo {
  font-size: 4em;
  font-weight: bold;
  margin-bottom: 20px;
  color: #00BFFF;
  text-shadow: 3px 3px 10px rgba(0, 191, 255, 0.7), 0 0 25px rgba(0, 191, 255, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  position: relative;
  user-select: none;
}

.headphones-icon-left, .headphones-icon-right {
  position: absolute;
  font-size: 2.5em;
  top: 0;
  z-index: -1;
  user-select: none;
}

.headphones-icon-left {
  left: -40px;
}

.headphones-icon-right {
  right: -40px;
}

.logo i {
  font-size: 1.5em;
}

.heartbeat-container {
  user-select: none;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 200px;
  position: relative;
}

.heartbeat {
  margin: 0 5px;
  border-radius: 5px;
  animation: heartbeat-animation 2s ease-in-out infinite;
  position: relative;
}

.heartbeat.long {
  width: 8px;
  height: 100px;
  background-color: #FF6347;
}

.heartbeat.short {
  width: 8px;
  height: 60px;
  background-color: #FF6347;
}

.heartbeat:nth-child(odd) {
  animation-delay: 0.1s;
}

.heartbeat:nth-child(even) {
  animation-delay: 0.3s;
}

@keyframes heartbeat-animation {
  0% {
    transform: scaleY(1);
  }
  25% {
    transform: scaleY(1.5);
  }
  50% {
    transform: scaleY(1);
  }
  75% {
    transform: scaleY(1.5);
  }
  100% {
    transform: scaleY(1);
  }
}

.welcome-btn {
  user-select: none;
  background-color: #00BFFF;
  color: white;
  font-size: 1.5em;
  font-weight: bold;
  padding: 10px 20px;
  border: 2px solid #00BFFF;
  border-radius: 30px;
  cursor: pointer;
  text-transform: uppercase;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 0 15px rgba(0, 191, 255, 0.5);
}

.welcome-btn:hover {
  background-color: transparent;
  color: #00BFFF;
  border-color: #00BFFF;
  box-shadow: 0 0 25px rgba(0, 191, 255, 1), 0 0 30px rgba(0, 191, 255, 0.7);
  transform: scale(1.1);
}
</style>
