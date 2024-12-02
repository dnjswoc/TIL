import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/Home/HomeView.vue'
import MoviesView from '@/views/Movie/MoviesView.vue'
import CommunityView from '@/views/Community/CommunityView.vue'
import LoginView from '@/views/Accounts/LoginView.vue'
import SingUpView from '@/views/Accounts/SingUpView.vue'
import CommunityMovieArticleView from '@/views/Community/CommunityMovieArticleView.vue'
import CommunityFreeArticleView from '@/views/Community/CommunityFreeArticleView.vue'
import CommunityFreeArticleCreateView from '@/views/Community/CommunityFreeArticleCreateView.vue'
import CommunityFreeArticleDetailView from '@/views/Community/CommunityFreeArticleDetailView.vue'
import FreeArticleUpdateForm from '@/components/Community/FreeArticle/FreeArticleUpdateForm.vue'
import { useAccountStore } from '@/stores/account';
import ProfileView from '@/views/Accounts/ProfileView.vue'
import ProfileUpdateView from '@/views/Accounts/ProfileUpdateView.vue'
import PasswordChange from '@/views/Accounts/PasswordChangeView.vue'
import IntroView from '@/views/Home/IntroView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
        path : '/',
        name : 'intro',
        component : IntroView
      },
      {
        path : '/home',
        name : 'home',
        component : HomeView
      },
      {
        path : '/movies',
        name : 'movies',
        component : MoviesView
      },
      {
        path : '/community',
        // name : 'community',
        component : CommunityView,
        children : [
          {path : '', name : 'community', component: CommunityMovieArticleView},
          {path : 'movie_article' , name : 'movie_article', component : CommunityMovieArticleView},
          // 자유게시판 게시글 전체 조회
          {path : 'free_article', name : 'free_article', component : CommunityFreeArticleView},
          // 자유게시판 게시글 생성
          {path : 'create', name : 'free_article_create', component : CommunityFreeArticleCreateView},
          // 영화추천게시판 게시글 생성
          // {path : 'create_movie', name : 'movie_article_create', compoenet : },
          // 자유게시판 게시글 상세 조회
          {path : ':free_article_id', name : 'free_article_detail', component : CommunityFreeArticleDetailView},
          // 자유게시판 게시글 수정
          {path : 'update/:free_article_id', name : 'update_free_article', component : FreeArticleUpdateForm}
        ]
      },

      {
        path : '/login',
        name : 'login',
        component : LoginView,
        beforeEnter: (to, from, next) => {
          const accountStore = useAccountStore();
          if (accountStore.token) {
            // 이미 로그인한 경우 홈 페이지로 리다이렉트
            next({ name: 'home' });
          } else {
            // 로그인하지 않은 경우 로그인 페이지로 이동 허용
            next();
          }
        }
      },
      {
        path : '/signup',
        name : 'signup',
        component : SingUpView
      },
      {
        path : '/profile',
        name : 'profile',
        component : ProfileView
      },
      {
        path : '/profile/update',
        name : 'profileUpdate',
        component : ProfileUpdateView
      },
      {
        path : '/profile/passwordchange',
        name : 'profilePasswordChange',
        component : PasswordChange
      }
  ],
  scrollBehavior() {
    return {
      top: 0
    }
  },
})

export default router

