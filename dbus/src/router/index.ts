import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import TwitterView from '../views/TwitterView.vue'
import WeatherView from '../views/WeatherView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import RouteStopInfoView from '../views/RouteStopInfoView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about/',
    name: 'about',
    component: AboutView
  },
  {
    path: '/login/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/twitter/',
    name: 'twitter',
    component: TwitterView
  },
  {
    path: '/weather/',
    name: 'weather',
    component: WeatherView
  },
  
  {
    path: '/register/',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/404/',
    name: '404',
    component: NotFoundView
  },
  {
    path: '/routeStopInfo/',
    name: 'routeStopInfo',
    component: RouteStopInfoView
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/404/',
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router