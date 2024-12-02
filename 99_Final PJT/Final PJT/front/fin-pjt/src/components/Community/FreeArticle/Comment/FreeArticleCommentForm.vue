<template>
  <div class="comment-section">
    <h4 class="comment-title">댓글</h4>
    <!-- 댓글 작성 폼 -->
    <form class="comment-form" @submit.prevent="addComment">
      <input
        type="text"
        class="comment-input"
        placeholder="댓글을 입력해주세요."
        v-model="newContent"
      />
      <button type="submit" class="submit-button">✔등록</button>
    </form>

    <hr />
    <p class="comment-count">댓글 수: <strong>{{ store.freeArticleCommentCount }}</strong>개</p>
    <!-- 댓글이 없는 경우 -->
    <div v-if="store.freeArticleCommentCount === 0" class="no-comment">
      <p>첫 댓글을 작성해주세요!</p>
    </div>

    <!-- 댓글 목록 -->
    <div v-else class="comment-list">
      <ul>
        <li
          v-for="comment in paginatedComments"
          :key="comment.id"
          :ref="setCommentRef(comment.id)"
          class="comment-item"
        >
          <div v-if="editingCommentId !== comment.id">
            <!-- 댓글 정보 -->
            <div class="comment-header">
              <span class="comment-author">
                작성자: {{ comment.user.nickname || comment.user.username }}
              </span>
            </div>
            <div class="comment-body">
              <p class="comment-content">{{ comment.content }}</p>
              <div class="button-group" v-if="userStore.isOwner(comment.user.id)">
                <button class="edit-button" @click="startEditing(comment.id, comment.content)">
                  ⚒수정
                </button>
                <button class="delete-button" @click="deleteComment(comment.id)">❌삭제</button>
              </div>
            </div>
            <div class="comment-dates">
              <small>작성일: {{ formatDate(comment.created_at) }}</small> |
              <small>수정일: {{ formatDate(comment.updated_at) }}</small>
            </div>
          </div>

          <!-- 댓글 수정 폼 -->
          <div v-else>
            <form @submit.prevent="updateComment(comment.id)">
              <input type="text" v-model="editingContent" class="comment-edit-input" />
              <div class="edit-buttons">
                <button type="submit" class="save-button">✔ 저장</button>
                <button type="button" @click="cancelEditing" class="cancel-button">❌ 취소</button>
              </div>
            </form>
          </div>
        </li>
      </ul>
    </div>

    <!-- 페이징 버튼 -->
    <div class="pagination" v-if="store.comments.length > pageSize">
      <button @click="prevPage" :disabled="currentPage === 1">이전</button>
      <span>페이지 {{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
    </div>
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { useAccountStore } from '@/stores/account';
import { onMounted, ref, computed, nextTick } from 'vue';
import { useRoute } from 'vue-router';

const store = useCommunityStore();
const userStore = useAccountStore();
const route = useRoute();

const newContent = ref('');
const editingCommentId = ref(null); // 현재 수정 중인 댓글 ID
const editingContent = ref(''); // 수정 중인 댓글 내용
const commentRefs = ref({}); // 각 댓글의 ref를 저장하는 객체

const currentPage = ref(1); // 현재 페이지
const pageSize = 3; // 페이지당 댓글 수

// 페이징 처리된 댓글 목록
const paginatedComments = computed(() => {
  const start = (currentPage.value - 1) * pageSize;
  const end = start + pageSize;
  return store.comments.slice(start, end);
});

// 총 페이지 수 계산
const totalPages = computed(() => Math.ceil(store.comments.length / pageSize));

// 댓글 작성
const addComment = function () {
  store.addFreeArticleComment(route.params.free_article_id, newContent.value);
  newContent.value = ''; // 댓글 작성 후 초기화

  // 새 댓글 페이지로 이동 및 포커싱
  currentPage.value = totalPages.value; // 마지막 페이지로 이동
  nextTick(); // DOM 업데이트 대기
  const lastCommentId = store.comments[store.comments.length - 1]?.id; // 새로 추가된 댓글 ID
  scrollToComment(lastCommentId);
};

// 댓글 삭제
const deleteComment = async (commentId) => {
  if (confirm('댓글을 삭제하시겠습니까?')) {
    store.deleteFreeArticleComment(route.params.free_article_id, commentId);

    // 현재 페이지 유지 및 갱신
    await nextTick(); // DOM 업데이트 대기
    const remainingComments = store.comments.length;
    const maxPage = Math.ceil(remainingComments / pageSize);
    if (currentPage.value > maxPage) {
      currentPage.value = maxPage || 1; // 최소 1페이지로 유지
    }
  }
};

// 댓글 수정 시작
const startEditing = (commentId, content) => {
  editingCommentId.value = commentId;
  editingContent.value = content;
};

// 수정 취소
const cancelEditing = () => {
  editingCommentId.value = null;
  editingContent.value = '';
};

// 댓글 수정
const updateComment = async (commentId) => {
  const originalComment = store.comments.find((comment) => comment.id === commentId)?.content;

  if (originalComment === editingContent.value.trim()) {
    alert('변경사항이 없습니다.');
    return;
  }

  if (confirm('댓글을 수정하시겠습니까?')) {
    await store.updateFreeArticleComment(route.params.free_article_id, commentId, editingContent.value);

    // 수정일 즉시 업데이트
    const updatedComment = store.comments.find((comment) => comment.id === commentId);
    if (updatedComment) {
      updatedComment.updated_at = new Date().toISOString(); // 현재 시간을 ISO 포맷으로 설정
    }

    cancelEditing();
  }
};

// 특정 댓글로 스크롤
const scrollToComment = (commentId) => {
  const element = commentRefs.value[commentId];
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
};

// 댓글 ref 저장
const setCommentRef = (id) => (el) => {
  if (el) {
    commentRefs.value[id] = el;
  }
};

// 페이징 이동
const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};

// 초기 데이터 가져오기
onMounted(() => {
  store.getFreeArticleComments(route.params.free_article_id);
});

// 날짜 및 시간 포맷팅
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
</script>

<style scoped>
.comment-section {
  margin-top: 30px;
  padding: 20px;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.85);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.comment-title {
  font-size: 1.5rem;
  margin-bottom: 20px;
  font-weight: bold;
  color: #333;
}

.comment-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.comment-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.comment-list {
  margin-top: 20px;
}

.comment-item {
  background-color: #f9f9f9;
  margin-bottom: 10px; /* 기존 15px에서 10px로 줄임 */
  padding: 10px; /* 기존 15px에서 10px로 줄임 */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  min-height: 120px; /* 카드의 최소 높이 설정 */
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.comment-author {
  font-weight: bold;
  color: #007bff;
  font-size: 1rem;
}

.comment-body {
  flex: 1; /* 댓글 본문을 남은 공간을 모두 차지하도록 설정 */
  margin-bottom: 10px; /* 본문과 다른 요소 사이의 여백 설정 */
  padding-left: 10px; /* 왼쪽 바와 본문 사이의 간격 조정 */
  border-left: 3px solid #007bff; /* 파란색 바의 두께 조절 */
}

.comment-dates {
  margin-top: auto; /* 댓글 아이템의 하단에 위치 */
  color: #555;
  font-size: 0.85rem;
  text-align: left; /* 텍스트를 왼쪽 정렬 */
}

.button-group {
  display: flex;
  justify-content: flex-end; /* 오른쪽 정렬 */
  gap: 10px; /* 버튼 간격 */
  margin-right: 5px;
}

.edit-button,
.save-button {
  background-color: #28a745;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 5px;
}

.delete-button,
.cancel-button {
  background-color: #ff4d4f;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.comment-edit-input {
  width: 100%; /* 댓글 수정 폼이 댓글 목록의 너비와 동일하게 설정 */
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box; /* 패딩 포함한 전체 너비를 맞추기 위함 */
}

.edit-buttons {
  display: flex;
  justify-content: flex-end; /* 오른쪽 정렬 */
  gap: 10px; /* 버튼 간격 */
  margin-top: 10px;
}

.pagination {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}
</style>
