import { createRouter, createWebHistory } from 'vue-router'
import GenreIdView from '@/views/GenreIdView.vue'
import MovieView from '@/views/MovieView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MovieView
    },
    {
      path: '/genre',
      name: 'genre',
      component: GenreIdView
    }
  ],
})

export default router
