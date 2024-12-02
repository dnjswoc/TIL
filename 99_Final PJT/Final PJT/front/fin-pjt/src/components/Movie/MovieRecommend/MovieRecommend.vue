<template>
  <div>
    <button @click="goToModal">
      영화 추천!
    </button>
    <MovieRecommendModal 
      v-if="isModalVisible"
      @close="closeModal"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRecommendStore } from '@/stores/recommend';
import MovieRecommendModal from './MovieRecommendModal.vue';

const store = useRecommendStore()

const movieRecommendList = store.movieRecommendList

const isModalVisible = ref(false);  // 모달 표시 여부

const goToModal = function () {
  isModalVisible.value = true // 모달 열기
}

// 모달 닫기
const closeModal = () => {
  isModalVisible.value = false;
  store.movieRecommendList = null
};


// onMounted(() => {
//   store.getMovieRecommend()
// })

</script>

<style scoped>

</style>