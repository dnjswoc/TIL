import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMovieStore = defineStore('movie', () => {
  const API_KEY = import.meta.env.VITE_TMDB_API_KEY

  return { API_KEY }
})
