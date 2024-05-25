<template>
  <nav class="navbar navbar-expand-lg bg-info">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">e &amp; LAN Events</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link active" aria-current="page">
              <a class="nav-link active">Home</a>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/locations" class="nav-link">
              <a class="nav-link">Location</a>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/events" class="nav-link">
              <a class="nav-link">Events</a>
            </router-link>
          </li>
          <li class="nav-item" v-if="authService.user.value">
            <router-link to="/registrations" class="nav-link">
              <a class="nav-link">Registrations</a>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link">
              <a class="nav-link">Login</a>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/account" class="nav-link">
              <a class="nav-link">Account</a>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import authService from "@/services/authService"
</script>

<style scoped>
.nav-link {
  color: rgb(23, 19, 19);
  font-size: 1em;
  background-color: rgba(229, 223, 223, 0.246);
  padding: 0em;
  border-radius: 50%;
  margin: 2.5em;
}

.navbar {
  padding: 0.2em 1rem;
}
</style>
