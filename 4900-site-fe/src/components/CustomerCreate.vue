<template>
    <div class="container-fluid">
      <div class="row align-items-center justify-content-center">
        <div class=" col align-items-center">
          <div class="row align-items-center justify-content-center">
            <div class="col col-12 col-sm-10 col-md-10 col-lg-6">
              <div class="alert alert-danger shadow" role="alert"
              v-if="showMsg === 'error'">
                Please verify Customer Information
              </div>
            </div>
          </div>
          <div class="row align-items-center justify-content-center">
            <div class="col col-12 col-sm-10 col-md-10 col-lg-6 align-items-center">
              <div class="card">
                <div class="card-header">{{pageTitle}}</div>
                <div class="card-body">
                  <form ref="form">
                    <div class="container-fluid">
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">Customer #</label>
                        <div class="col col-8">
                          <input v-model="customer.cust_number" type="number" class="form-control-sm form-control">
                        </div>
                      </div>
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">Name</label>
                        <div class="col col-8">
                          <input v-model="customer.name" type="text" class="form-control-sm form-control">
                        </div>
                      </div>          
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">Address</label>
                        <div class="col col-8">
                          <input v-model="customer.address" type="text" class="form-control-sm form-control">
                        </div>
                      </div>
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">City</label>
                        <div class="col col-8">
                          <input v-model="customer.city" type="text" class="form-control-sm form-control">
                        </div>
                      </div> 
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">State</label>
                        <div class="col col-8">
                          <input v-model="customer.state" type="text" class="form-control-sm form-control">
                        </div>
                      </div>
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">Zip Code</label>
                        <div class="col col-8">
                          <input v-model="customer.zipcode" type="text" class="form-control-sm form-control">
                        </div>
                      </div>
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">Email</label>
                        <div class="col col-8">
                          <input v-model="customer.email" type="text" class="form-control-sm form-control">
                        </div>
                      </div>
                      <div class="form-group row justify-content-around py-2">
                        <label class="col-4">Phone</label>
                        <div class="col col-8">
                          <input v-model="customer.cell_phone" type="text" class="form-control-sm form-control">
                        </div>
                      </div>                    
                      <div class="row justify-content-around">
                        <div v-if="!isUpdate" type="button" class="btn btn-primary col-4" @click="createCustomer">Save</div>
                        <div v-if="isUpdate" type="button" class="btn btn-primary col-4" @click="updateCustomer">Update</div>
                        <div type="button" class="btn btn-secondary col-4" @click="cancelOperation">Cancel</div>   
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  <script>
    import router from '../router';
    import {APIService} from '../http/APIService';
    const apiService = new APIService();
  
    export default {
      name: 'CustomerCreate',
      components: {},
          //prevent user from accessing this page if not authorized
    beforeCreate() {
    if (localStorage.getItem("isAuthenticated") &&
        JSON.parse(localStorage.getItem("isAuthenticated")) === true ){
          this.authenticated = true
        }
        else {
          this.authenticated = false
        }
        if(this.authenticated===false){
            router.push("/auth");
          }
   },
      data() {
        return {
          showError: false,
          customer: {},
          pageTitle: "Add New Customer",
          isUpdate: false,
          showMsg: '',
          authenticated: false
        };
      },
      methods: {
        createCustomer() {
          apiService.addNewCustomer(this.customer).then(response => {
            if (response.status === 201) {
              this.customer = response.data;
               this.showMsg = "";
              router.push('/customer-list/new');
            }else{
                this.showMsg = "error";
            }
          }).catch(error => {
            if (error.response.status === 401) { // "not authorized"
              router.push("/auth");
            }else if (error.response.status === 400) { //"bad request"
              this.showMsg = "requestError";
            }else{
              this.showMsg = "error";
            }
          });
        },
        cancelOperation(){
           router.push("/customer-list");
        },
        updateCustomer() {
          apiService.updateCustomer(this.customer).then(response => {
            if (response.status === 200) {
              this.customer = response.data;
              router.push('/customer-list/update');
            }else{
                this.showMsg = "error";
            }
          }).catch(error => {
            if (error.response.status === 401) {
              router.push("/auth");
            }else if (error.response.status === 400) {
              this.showMsg = "error";
            }
          });
        }
      },
      mounted() {
        if (this.$route.params.pk) {
          this.pageTitle = "Edit Customer";
          this.isUpdate = true;
          apiService.getCustomer(this.$route.params.pk).then(response => {
            this.customer = response.data;
          }).catch(error => {
            if (error.response.status === 401) { // "not authorized"
              router.push("/auth");
            }else{
              this.showMsg = "error";
              router.push("/auth");
            }
          });
        }
      },
    }
  </script>
 

