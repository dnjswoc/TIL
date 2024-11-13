<template>
  <div>
    <span 
    @click="store.updateTodo(todo.id)"
    :class="{ 'is-done': todo.isDone }"
    >
      {{ todo.text }}
    </span>
    <button @click="store.deleteTodo(todo.id)">삭제</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

defineProps({
  todo: Object
})

const store = useCounterStore()

</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>