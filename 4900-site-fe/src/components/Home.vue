<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col col-12 align-items-center justify-content-center">
                <blockquote>
                    &#8220;Welcome {{validUserName}}!&#8221;
                    <footer>
                    <small>
                        <em>&mdash;Welcome to our Smokehouse!</em>
                    </small>
                    </footer>
                </blockquote>
            </div>
        </div>
    </div>
    <div class="container-fluid">
        <div class="row align-items-center justify-content-center">
            <div class="col col-12 col-sm-10 col-md-10">
                <div class="card-group">
                <div class="card">
                  <img :src="require('@/assets/menu.png')" class="card-img-top" style="height: 15rem">
                  <div class="card-body">
                    <h5 class="card-title">Menu</h5>
                    <a @click="Menu" class="btn btn-primary">Show Menu</a>
                  </div>
                </div>
                <div class="card">
                  <img :src="require('@/assets/pulled_pork.jpeg')" class="card-img-top" style="height: 15rem">
                  <div class="card-body">
                    <h5 class="card-title">Photos</h5>
                    <a @click="viewInvestments" class="btn btn-primary">Show Photos</a>
                  </div>
                </div>
                <div class="card">
                  <img :src="require('@/assets/book_reservation.png')" class="card-img-top" style="height: 15rem">
                  <div class="card-body">
                    <h5 class="card-title">Reserve</h5>
                    <a @click="viewStocks" class="btn btn-primary">Make Reservation</a>
                  </div>
                </div>
              </div>
            </div>
        </div>
    </div>
</template>
<script>
import router from '../router'
export default {
    name: 'Home',
    beforeCreate() {
    if (localStorage.getItem("isAuthenticated") &&
        JSON.parse(localStorage.getItem("isAuthenticated")) === true ){
          this.authenticated = true
        }
        else {
          this.authenticated = false
        }
   },
    data: () => ({
      validUserName: "Guest",
      authenticated: false
    }),
    mounted() {
      this.getUser();
    },
    methods: {
      // viewCustomers() {
      //   router.push('/customer-list');
      // },
      // viewInvestments() {
      //   router.push('/customer-list');
      // },
      // viewStocks() {
      //   router.push('/customer-list');
      // },
      getUser() {
        if (localStorage.getItem("isAuthenticated")
          && JSON.parse(localStorage.getItem("isAuthenticated")) === true) {
          this.validUserName = JSON.parse(localStorage.getItem("log_user"));
          this.authenticated = true;
        }
      }
    }
  }
</script>
