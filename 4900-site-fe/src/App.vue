<template>
  <ul class="nav justify-content-end">
     <div class="SB"><emp>Smokey's Barbeque </emp></div>
     <li class="nav-item active">
         <router-link to="/">Home</router-link> |
     </li>
     <li class="nav-item">
         <router-link :to="{name: 'Menu'}">Menu</router-link> |
     </li>
     <li class="nav-item" v-if="!authenticated" @click="register" >
         <router-link :to="{name: 'Register'}">Register</router-link> |
     </li>
     <li class="nav-item" v-if="!authenticated" @click="login" >
         <router-link :to="{name: 'Auth'}">Log in</router-link>
     </li>
     <li class="nav-item  .justify-content-end" v-if="authenticated" @click="logout" >
         <router-link :to="{name: 'Auth'}">Logout</router-link>
     </li>
 </ul>
 <router-view/>
</template>
<script>
 import router from './router';
 import {APIService} from './http/APIService';
 const apiService = new APIService();

 export default {
     name: 'App',
     data: () => ({
         authenticated: false,
         dialog: false,
         menu: [
             { title: 'Home', url:"/"},
             { title: 'Menu', url:"/menu" },
         ]
     }),
     mounted() {
       if (localStorage.getItem("isAuthenticated") &&
           JSON.parse(localStorage.getItem("isAuthenticated")) === true ){
           this.authenticated = true
       }else {
           this.authenticated = false
       }
       if(this.authenticated === true) {
         apiService.getCustomerList().then(response => {
             this.authenticated = true;
         }).catch(error => {
             if (error.response.status === 401) {
               localStorage.clear();
               localStorage.setItem("isAuthenticated", false);
               this.authenticated = false;
             }
         });
       } 
     },
     methods: {
       getUser() {
           if (localStorage.getItem("isAuthenticated") &&
            JSON.parse(localStorage.getItem("isAuthenticated")) === true
           ) {
            this.validUserName = JSON.parse(localStorage.getItem("log_user"));
            } 
       },
         logout() {
           //clear local storage items and set authenticated to false
           localStorage.clear();
           localStorage.setItem("isAuthenticated", false);
           this.authenticated = false;
           window.location = "/";
         },
         login() {
             router.push("/auth");
         },
         home() {
           window.location = "/";
           },
       register() {
           router.push("/register");
       }
   }
}
</script>
<style lang="scss">
 #app {
     font-family: Avenir, Helvetica, Arial, sans-serif;
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
     text-align: center;
     color: black;
 }
 #nav {
     padding: 30px;
     background-color: #442027;
     a {
         font-weight: bold;
         color: #FFF4C3;
         &.router-link-exact-active {
             color: #FFF4C3;
         }
     }
 }
 .nav {
     padding: 1em;
     background-color: #442027;
     
     li {
         font-weight: bold;
         color: #FFF4C3;
     }
     a {
         color: #FFF4C3;
         padding: .5em;

         &.router-link-exact-active {
             color: #FFF4C3;
         }
     }
     .SB{
         margin-right: 45em;
         font-size: medium;
         color: #FFF4C3
     }
 }
</style>