import { createRouter, createWebHashHistory } from "vue-router"
import HomeView from "../views/HomeView.vue"

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView
    },
    {
      path: "/locations",
      name: "locations",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ "../views/LocationsView.vue")
    },
    {
      path: "/events",
      name: "events",
      component: () => import("../views/EventsView.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/Login.vue")
    },
    {
      path: "/account",
      name: "account",
      component: () => import("../views/AccountView.vue")
    },
    {
      path: "/registrations",
      name: "registrations",
      component: () => import("../views/EventRegistration.vue")
    }
  ]
})

export default router
