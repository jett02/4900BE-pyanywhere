import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Auth from '@/components/Auth.vue'
import Reservations from '@/components/Reservations.vue'
import Register from '@/components/Register'
import Menu from '@/components/Menu'
import CustomerCreate from '@/components/CustomerCreate'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/menu',
    name: 'Menu',
    component: Menu
  },
  // {
  //   path: '/customer-list/:msg',
  //   name: 'CustomerUpdatedList',
  //   component: CustomerList
  // },
  {
    path: '/customer-create',
    name: 'CustomerCreate',
    component: CustomerCreate
  },
  {
    path: '/customer-create/:pk',
    name: 'CustomerUpdate',
    component: CustomerCreate
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  },
  {
    path:'/register',
    name: 'Register',
    component: Register
  },
  {
    path:'/reservations',
    name: 'Reservations',
    component: Reservations
  } 

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
