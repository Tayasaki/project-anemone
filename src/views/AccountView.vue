<template>
  <div class="hello">
    <br />
    <div v-if="user" class="container">
      <div class="alert alert-success">
        <p>Logged in successfully!</p>
      </div>
      <form>
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" class="form-control" v-model="username" placeholder="Username" />
        </div>
        <div class="form-group">
          <label for="firstname">First Name:</label>
          <input type="text" class="form-control" v-model="first_name" placeholder="First Name" />
        </div>
        <div class="form-group">
          <label for="lastname">Last Name:</label>
          <input type="text" class="form-control" v-model="last_name" placeholder="Last Name" />
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" class="form-control" v-model="email" placeholder="Email" />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" class="form-control" v-model="password" placeholder="Password" />
        </div>
        <div class="form-group">
          <button class="btn btn-primary" @click="save">Save</button>
          <button class="btn btn-secondary" @click="logout">Logout</button>
        </div>
      </form>
      <br />
    </div>
    <div v-else class="container">
      <p>You need to be logged in</p>
      <router-link :to="{ name: 'login' }" class="btn btn-primary">Login</router-link>
    </div>
  </div>
</template>

<script>
import authService from "../services/authService"

export default {
  name: "AccountView",
  data() {
    return {
      username: "",
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      loginError: ""
    }
  },
  computed: {
    user() {
      return authService.user.value
    }
  },
  methods: {
    logout() {
      authService.logout()
    },
    save() {
      authService.updateUserInfo({
        username: this.username,
        password: this.password,
        email: this.email,
        first_name: this.first_name,
        last_name: this.last_name
      })
    },
    fetchUserInfo() {
      this.username = authService.user.value.username
      this.first_name = authService.user.value.first_name
      this.last_name = authService.user.value.last_name
      this.email = authService.user.value.email
      this.password = authService.user.value.password
    }
  },
  async mounted() {
    await authService.checkToken()
    if (this.user) {
      this.fetchUserInfo()
    }
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
