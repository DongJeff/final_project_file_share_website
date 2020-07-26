import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('../views/index.vue')
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import('../views/signUp.vue')
  },
  {
    path: '/download',
    name: 'Download',
    component: () => import('../views/downLoad.vue')
  }
]

var router =  new VueRouter({
  routes
})

export default router
