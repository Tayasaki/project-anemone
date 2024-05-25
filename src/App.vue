<template>
  <NavbarVue />
  <router-view />
  <FooterVue />
</template>
<script>
import NavbarVue from "@/components/NavbarVue.vue"
import FooterVue from "./components/FooterVue.vue"
import authService from "@/services/authService"

export default {
  name: "App",
  components: {
    NavbarVue,
    FooterVue
  },
  mounted() {
    authService.checkToken()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
