import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Layout from '@/components/Layout.vue'
import BlogPage from '@/pages/BlogPage.vue'
import MainPage from '@/pages/MainPage.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: MainPage, 
  },
  {
    path: '/blog/:category',
    name: 'BlogPage',
    component: BlogPage, 
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
