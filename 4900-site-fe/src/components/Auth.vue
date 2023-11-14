<template>
    <div class="container">
    <div class="row align-items-center justify-content-center">
      <div class="col-12 col-sm-6 col-md-4 col-lg-4">
        <div class="card mx-auto shadow">
          <div class="card-body">
            <div class="card-title"><span>Login</span></div>
            <div
              v-if="showMsg === 'loginError'"
              close-icon="mdi-close-circle"
              :value="true"
              class="alert alert-danger"
              role="alert"
              dense
            >
              Invalid username or password. Please Try again.
            </div>
            <div
              v-else-if="showMsg === 'axiosError'"
              close-icon="mdi-close-circle"
              :value="true"
              class="alert alert-danger"
              role="alert"
              dense
            >
              Access blocked by server. Check server.
            </div>
            <div class="card-text pt-2">
              <div class="col-md-10 mb-3">
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text">@</span>
                  </div>
                  <input
                    v-model="credentials.username"
                    :counter="70"
                    label="Username"
                    :rules="rules.username"
                    maxlength="70"
                    required
                    type="text"
                    class="form-control mb-3"
                    placeholder="Username"
                    aria-describedby="inputGroupPrepend2"
                  />
                  <div class="w-100"></div>
                  <div class="input-group-prepend">
                    <span class="input-group-text">***</span>
                  </div>
                  <input
                    :type="showPassword ? 'text' : 'Password'"
                    v-model="credentials.password"
                    label="Password"
                    :rules="rules.password"
                    maxlength="20"
                    required
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="showPassword = ! showPassword"
                    class="form-control"
                    placeholder="Password"
                    aria-describedby="inputGroupPrepend2"
                  />
                </div>
              </div>
              <button ref ="form" @click.prevent="login" class="btn btn-primary">Login</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
  
  <script>
  import router from '../router';
  import { APIService } from "../http/APIService";
  const apiService = new APIService();
  
  export default {
  name: "Auth",
  data: () => ({
      credentials: {},
      valid: true,
      showMsg: "",
      loading: false,
      rules: {
        username: [
          (v) => !!v || "Username is required",
          (v) =>
            (v && v.length > 3) ||
            "A username must be more than 3 characters long",
          (v) =>
            /^[a-z0-9_]+$/.test(v) ||
            "A username can only contain letters and digits",
        ],
        password: [
          (v) => !!v || "Password is required",
          (v) =>
            (v && v.length > 7) ||
            "The password must be longer than 7 characters",
        ],
      },
      showPassword: false,
    }),
    methods: {
      login(){
            localStorage.clear();
            localStorage.setItem("isAuthenticated", false)
  
            apiService
            .authenticateLogin(this.credentials)
            .then((response) => {
                const access = response.data.access
                const refresh = response.data.refresh
  
                localStorage.setItem("access", access)
                localStorage.setItem("refresh",refresh)
                localStorage.setItem("isAuthenticated", true)
                localStorage.setItem("log_user", JSON.stringify(this.credentials.username))
        
                window.location = "/";
          }).catch(error => {
          if (error.message ==="Network Error"){ // Verify CORS middleware installed in server settings
            this.showMsg = "axiosError"
          }else if (error.response.status === 401) { // "not authorized"
              this.showMsg = "loginError";
              router.push("/auth");
            }else if (error.response.status === 400) { //"bad request"
              this.showMsg = "loginError";
            }else{
              this.showMsg = "axiosError";
              router.push("/auth");
            }
        });
        }
    }
  }
  </script>
  