<template>
  <div class="hello">
    <br />
    <div v-if="user" class="container">
      <div class="alert alert-success">Logged in successfully!</div>
      <router-link :to="{ name: 'account' }" class="btn btn-primary">Account</router-link>
      <br />
    </div>
    <div v-else class="container">
      <p>You need to be logged in</p>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" class="form-control" v-model="username" placeholder="Username" />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" class="form-control" v-model="password" placeholder="Password" />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" v-model="email" placeholder="Email" />
      </div>
      <button class="btn btn-primary" @click="register">Register</button>
      <button class="btn btn-primary" @click="login">Login</button>
      <p v-if="loginError" class="alert alert-danger">{{ loginError }}</p>
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
      email: "",
      loginError: ""
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    login() {
      this.loginError = ""
      authService
        .login({
          username: this.username,
          password: this.password
        })
        .catch((err) => {
          this.loginError = err.response.data
        })
    },
    register() {
      this.loginError = ""
      authService
        .register({
          username: this.username,
          password1: this.password,
          password2: this.password,
          email: this.email
        })
        .catch((err) => {
          if (err.response.status === 500) return
          this.loginError = err.response.data
        })
    }
  },
  async mounted() {
    await authService.checkToken()
  }
}
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: auto;
}

.form-group {
  margin-bottom: 20px;
}

.btn-primary {
  margin-right: 10px;
}

.alert {
  margin-bottom: 20px;
}

.alert p {
  margin-bottom: 0;
}
</style>
