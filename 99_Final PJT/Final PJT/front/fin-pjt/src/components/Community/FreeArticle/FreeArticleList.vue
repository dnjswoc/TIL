<template>
  <div class="free-article-table">
    <table>
      <thead>
        <tr>
          <th>No.</th>
          <th>제목</th>
          <th>작성자</th>
          <th>작성일</th>
          <th>보기</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(freearticle, index) in paginatedArticles" :key="freearticle.id">
          <td>{{ startIndex + index + 1 }}</td>
          <td>{{ freearticle.title ? freearticle.title : '제목이 없습니다.' }}</td>
          <td>{{ freearticle.user.nickname ? freearticle.user.nickname : freearticle.user.username }}</td>
          <td>{{ formatDate(freearticle.created_at) }}</td>
          <td>
            <!-- 게시글 상세 페이지로 가기 -->
            <button @click="viewArticle(freearticle.id)">보기</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 페이징 버튼 -->
    <div class="pagination" v-if="totalPages > 1">
      <button :disabled="currentPage === 1" @click="prevPage">이전</button>
      <span>페이지 {{ currentPage }} / {{ totalPages }}</span>
      <button :disabled="currentPage === totalPages" @click="nextPage">다음</button>
    </div>
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { useRouter } from 'vue-router';
import { ref, computed, onMounted } from 'vue';

const store = useCommunityStore();
const router = useRouter();

const currentPage = ref(1); // 현재 페이지
const pageSize = 6; // 페이지당 게시글 수

// 게시글 데이터 페이징 처리
const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * pageSize;
  const end = start + pageSize;
  return store.freearticles.slice(start, end);
});

// 총 페이지 수 계산
const totalPages = computed(() => Math.ceil(store.freearticles.length / pageSize));

// 현재 페이지의 시작 인덱스
const startIndex = computed(() => (currentPage.value - 1) * pageSize);

// 페이지 이동 함수
const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};

// 게시글 보기 함수
const viewArticle = (id) => {
  router.push({ name: 'free_article_detail', params: { free_article_id: id } });
};

// 작성일 포맷팅 함수
const formatDate = (date) => {
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  };
  return new Date(date).toLocaleString('ko-KR', options);
};

onMounted(() => {
  store.getfreeArticles(); // 게시글 목록 가져오기
});
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); 


/* 테이블 컨테이너 */
.free-article-table {
  margin: 70px auto;
  max-width: 100%;
  text-align: center;
  user-select: none;
}
/* 테이블 스타일 */
table {
  width: 100%;
  border-collapse: collapse; /* 테두리 겹침 제거 */
  background-color: #f9f9f9; /* 테이블 배경색 */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
  border-radius: 10px;
  overflow: hidden;
}

/* 테이블 헤더 스타일 */
thead {
  font-family: 'Arial', sans-serif;
  font-size: 2.1em; /* 적당한 크기로 줄임 */
  font-weight: bold;
  background-color: #151314;
  color: white;
}

thead th {
  padding: 20px;
  font-size: 1.2rem;
  text-align: center;
}

/* 테이블 본문 스타일 */
tbody td {
  font-family: 'Arial', sans-serif;
  font-size: 1.1rem; /* 적당한 크기로 줄임 */
  font-weight: bold;
  padding: 20px;
  border-bottom: 1px solid #ddd;
  text-align: center;
}

/* 마지막 줄의 테두리 제거 */
tbody tr:last-child td {
  border-bottom: none;
}

/* 버튼 스타일 */
button {
  background-color: #151314;
  color: white;
  font-size: 0.9rem;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

button:hover:enabled {
  background-color: #0056b3;
}

/* 페이징 스타일 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-top: 15px;
}

.pagination span {
  font-size: 1rem;
  font-weight: bold;
}
</style>
