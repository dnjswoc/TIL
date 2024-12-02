<template>
  <!-- 한줄평 작성 폼 -->
  <form v-if="!hasWrittenComment" @submit.prevent="addMovieComment" class="comment-form">
    <div class="rating-container">
      <div class="rating">
        <span
          v-for="star in 5"
          :key="star"
          class="star"
          :class="{ 
            active: star <= store.newComment.rating 
          }"
          @click="toggleRating(star)"
        >
          ★
        </span>
      </div>
    </div>
    <div class="input-container">
      <textarea
        v-model="store.newComment.content"
        placeholder="영화 한줄평 남과주세요."
        required
      ></textarea>
    </div>
    <input type="submit" value="등록" class="submit-btn" />
  </form>

  <!-- 이미 작성한 한줄평 알림 -->
  <div v-if="hasWrittenComment" class="alert">
    <p>이미 한줄평을 작성한 영화입니다! 😊</p>
  </div>
  <hr>
  <!-- 한줄평 개수 및 평균 평점 -->
  <div class="summary-container">
    <p>총 <strong>{{ store.movieCommentsCount }}</strong> 건 | 평점: <strong>{{ averageScore.toFixed(1) }}</strong> / 5.0 점</p>
  </div>

  <!-- 한줄평 목록 -->
  <div v-if="store.movieCommentsCount === 0">
    <p class="no-comments">첫 한줄평을 작성해주세요!</p>
  </div>
  <div v-else>
    <ul>
      <li v-for="comment in store.movieComments" :key="comment.id" class="comment-item">
        <div v-if="editingCommentId === comment.id">
          <!-- 수정 폴 -->
          <div class="rating">
            <span
              v-for="star in 5"
              :key="'edit-star-' + star"
              class="star"
              :class="{ active: star <= editingRating, editable: true }"
              @click="toggleRating(star)"
            >
              ★
            </span>
            <textarea v-model="editingContent" class="edit-textarea"></textarea>
          </div>
          
          <div class="action-buttons">
            <button @click="saveEditedComment" class="edit-btn">✔ 저장</button>
            <button @click="cancelEditing" class="delete-btn">❌ 취소</button>
          </div>
        </div>
        <div v-else>
          <!-- 별점과 한줄평 -->
          <div class="readonly">
            <span
              v-for="star in 5"
              :key="'star-' + star"
              class="star"
              :class="{ active: star <= comment.score }"
            >
              ★
            </span>
            <p class="comment-content">{{ comment.content }}</p>
          </div>

          <!-- 작성자와 작성일 -->
          <p class="comment-meta">작성자: {{ comment.user.nickname }}</p>
          <p class="comment-date">{{ formatDate(comment.created_at) }}</p>

          <!-- 수정 및 삭제 버튼 -->
          <div v-if="userStore.isOwner(comment.user.id)" class="action-buttons">
            <button @click="startEditing(comment)" class="edit-btn">⚒ 수정</button>
            <button @click="deleteMovieComment(comment.id)" class="delete-btn">❌ 삭제</button>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { defineProps, watch, ref, computed } from 'vue';
import { useRoute } from 'vue-router'
import { useAccountStore } from '@/stores/account'

const store = useMovieStore();
const route = useRoute()
const userStore = useAccountStore()

const props = defineProps({
  movieId: Number, 
});

const hasWrittenComment = computed(() => {
  return store.movieComments.some(comment => comment.user.id === userStore.userId.id);
});

const addMovieComment = function () {
  store.addMovieComment(props.movieId);
};

const deleteMovieComment = function (commentId) {
  if (confirm('한줄평을 삭제하시겠습니까?')) {
    store.deleteMovieComment(props.movieId, commentId);
  }
}

const editingCommentId = ref(null);
const editingContent = ref('');
const editingRating = ref(0);

const startEditing = (comment) => {
  editingCommentId.value = comment.id;
  editingContent.value = comment.content;
  editingRating.value = comment.score;
  setEditingState(true);
};

const cancelEditing = () => {
  editingCommentId.value = null;
  editingContent.value = '';
  editingRating.value = 0;
  setEditingState(false);
};

const saveEditedComment = () => {
  const originalComment = store.movieComments.find(
    (comment) => comment.id === editingCommentId.value
  );

  if (originalComment.content === editingContent.value && originalComment.score === editingRating.value) {
    alert('변경된 내용이 없습니다.');
    return;
  }

  const updatedComment = {
    content: editingContent.value,
    score: editingRating.value,
  };
  store.editMovieComment(props.movieId, editingCommentId.value, updatedComment);
  cancelEditing();
};

const toggleRating = (star) => {
  if (editingCommentId.value !== null) {
    editingRating.value = editingRating.value === star ? 0 : star;
  } else {
    store.newComment.rating = store.newComment.rating === star ? 0 : star;
  }
};

const setEditingState = (state) => {
  const ratingContainer = document.querySelector('.rating-container');
  const textarea = document.querySelector('textarea');
  const stars = document.querySelectorAll('.rating-container .star');
  
  if (state) {
    textarea.focus();
    ratingContainer.classList.add('editing');
    stars.forEach(star => {
      star.classList.add('editable');
    });
  } else {
    ratingContainer.classList.remove('editing');
    stars.forEach(star => {
      star.classList.remove('editable');
    });
  }
};

watch(
  () => props.movieId,
  (newMovieId) => {
    if (newMovieId) {
      store.getMovieComments(newMovieId);
    }
  },
  { immediate: true }
);

const formatDate = (date) => {
  if (!date) return '';
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  };
  return new Date(date).toLocaleString('ko-KR', options);
}

const averageScore = computed(() => {
  if (store.movieComments.length === 0) return 0;
  return store.movieComments.reduce((total, comment) => total + comment.score, 0) / store.movieComments.length;
});
</script>

<style scoped>
/* 한줄평 작성 폴 */
.comment-form {
  display: flex;
  align-items: flex-start;
  gap: 1rem; /* 간격 확대 */
  justify-content: flex-start;
  margin-bottom: 1.5rem; /* 폴과 리스트 간격 추가 */
  background: #f9f9f9;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 한줄평 없음 메시지 */
.no-comments {
  color: #ffffff; /* 힌색 텍스트로 변경하여 어두운 배경에서 가득성 확대 */
  font-size: 1.2rem;
  text-align: center;
}
.rating-container {
  display: flex;
  justify-content: flex-start;
}

.input-container {
  flex: 2;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
}

textarea {
  width: 100%;
  height: 100px;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  font-size: 1rem;
  outline: none;
}

.submit-btn {
  flex-shrink: 0;
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #45a049;
}

/* 한줄평 목록 */
.comment-list {
  list-style: none;
  padding: 0;
}

.comment-item .readonly {
  display: flex;
  align-items: baseline; /* 별과 한줄평 녹이를 맞음 */
  gap: 0.1rem; /* 별과 한줄평 사이 간격 */
}

.readonly .star {
  display: inline-block;
  font-size: 1.5rem;
  line-height: 1; /* 별의 녹이를 텍스트와 맞음 */
  margin-right: 0.1rem; /* 별 간 간격을 줄임 */
  color: #aaa; /* 기본 색상 (선택되지 않은 별) */
}

.comment-content {
  margin: 0; /* 한줄평 텍스트의 여배 제거 */
  padding-left: 18px;
  line-height: 1.5; /* 텍스트의 줄 녹이 조정 */
  font-size: 1rem; /* 텍스트 크기 */
  white-space: nowrap; /* 한줄로 표시, 필요 시 텍스트 줄바꿈을 막지 */
  overflow: hidden; /* 텍스트가 너무 길 경우 */
  text-overflow: ellipsis; /* 길어지는 경우 말줄임표 처리 */
  color: #ffffff; /* 힌색 텍스트로 변경 */
}

/* 한줄평 리스트 */
.comment-item {
  background-color: rgba(255, 255, 255, 0.1); /* 상당히 투명한 힌색 배경 */
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  color: #ffffff; /* 텍스트를 힌색으로 변경 */
}

.comment-meta,
.comment-date {
  font-size: 0.9rem;
  color: #777;
  margin-top: 1rem; /* 상단 여배 */
}
/* 별점 */
.rating {
  display: flex;
}

.star {
  font-size: 1.5rem;
  color: #ddd;
}

.star.active {
  color: gold;
}

/* 수정/삭제 버튼 */
.action-buttons {
  margin-top: 10px;
  text-align: right;
}

/* 수정 상태의 별점과 텍스트 연구 스타일 */
.readonly {
  display: flex;
  flex-direction: row; /* 별점과 폴미 거래로 배치 */
  align-items: center; /* 위접 정렬 */
  gap: 0.8rem; /* 별점과 폴 간 간격 */
}

/* 별점 스타일 */
.readonly .star {
  display: inline-block;
  font-size: 1.5rem; /* 별 크기 */
  line-height: 1; /* 별의 녹이 조정 */
  margin-right: 0.03rem; /* 별 사이 간격을 짘임 */
  color: #bbb; /* 비활성 별 색상 */
  
}

.readonly .star.active {
  color: gold; /* 활성화된 별 색상 */
}

/* 한줄평 텍스트 스타일 */
.comment-content {
  margin: 0; /* 여배 제거 */
  line-height: 1.5; /* 줄 녹이 조정 */
  font-size: 1rem; /* 텍스트 크기 */
  color: #ffffff; /* 한줄평 텍스트 색상 */
}


.rating {
  display: flex;
  flex-direction: row;
  gap: 0.3rem; /* 별 사이 간격 */
}

.edit-textarea {
  flex: 1; /* 텍스트 입력 폴미 남은 곳과 착이 */
  height: 120px;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  font-size: 1rem;
  outline: none;
}

.star {
  font-size: 1.5rem;
  color: #ddd;
  cursor: pointer;
}

.star.active {
  color: gold;
}

.summary-container p {
  color: #ffffff; /* 요약 텍스트 힌색으로 변경 */
}

/* 수정 및 삭제 버튼 */
.action-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}

.edit-btn,
.delete-btn {
  padding: 0.4rem 0.8rem;
  border: none;
  border-radius: 4px;
  font-size: 0.85rem;
  cursor: pointer;
}

.edit-btn {
  background-color: #4CAF50; /* 기본 초록색 */
  color: white;
  transition: background-color 0.3s ease; /* 부드러운 색상 전환 */
}

.edit-btn:hover {
  background-color: #388E3C; /* 어두운 초록색 */
}

.delete-btn {
  background-color: #dc3545;
  color: white;
}

.delete-btn:hover {
  background-color: #c82333;
}
/* 이미 작성한 한줄평 메시지 */
.alert {
  background-color: #ffeeba; /* 부드러운 녹화색 배경 */
  color: #856404; /* 다소 어두운 텍스트 */
  border: 1px solid #ffc107; /* 짓은 테두리 */
  padding: 1rem;
  border-radius: 8px; /* 들지기 모세리 */
  font-size: 1rem;
  font-weight: bold;
  text-align: center; /* 텍스트 가운데 정렬 */
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* 약간의 그림자 */
  margin: 1.5rem 0; /* 위안에 간격 */
  animation: fadeIn 0.5s ease; /* 나타나는 때 페이드 인 효과 */
}

/* 페이드 인 애니메이션 */
@keyframes fadeIn {
  from {
    opacity: 0; /* 투명하게 시작 */
    transform: translateY(-10px); /* 위에서 아래로 이동 */
  }
  to {
    opacity: 1; /* 완전히 나타날 */
    transform: translateY(0); /* 원래 위치로 */
  }
}

</style>
