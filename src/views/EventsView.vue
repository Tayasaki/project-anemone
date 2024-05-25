<template>
  <div>
    <div id="root" class="py-4">
      <div class="row">
        <div v-if="authService.user.value" class="col-md-3">
          <h2>Events</h2>
          <div class="card card-body">
            <form ref="userForm">
              <div class="form-group">
                <input
                  type="text"
                  ref="name"
                  v-model="event.name"
                  class="form-control"
                  placeholder="Event name"
                  minlength="5"
                  maxlength="50"
                  required
                />
              </div>
              <div class="form-group">
                <input
                  type="text"
                  v-model="event.description"
                  class="form-control"
                  placeholder="Description"
                  minlength="10"
                  maxlength="200"
                  required
                />
              </div>
              <div>
                <input
                  type="checkbox"
                  v-model="event.lan"
                  class="form-check-input"
                  placeholder="Lan"
                  required
                />
                <label class="form-check-label" for="lan">Lan</label>
              </div>
              <select v-model="event.location" class="form-select" required>
                <option value="" disabled selected>Select location</option>
                <option v-for="location in locations" :key="location.id" :value="location.id">
                  {{ location.name }}
                </option>
              </select>
              <div>
                <input
                  type="number"
                  v-model="event.capacity"
                  class="form-control mb-3"
                  placeholder="Start date"
                  required
                />
              </div>
              <div>
                <input
                  type="date"
                  v-model="event.date"
                  class="form-control mb-3"
                  placeholder="Start date"
                  required
                />
              </div>
              <p v-if="!isNotEmpty">All fields are required</p>
              <div class="form-group">
                <input
                  type="button"
                  :disabled="!isNotEmpty"
                  @click="addEvent"
                  class="btn btn-success btn-block text-dark"
                  value="Add Event"
                />
              </div>
            </form>
          </div>
        </div>
        <div class="form-group col-md-9 text-left">
          <h3 class="text-start text-warning">Search</h3>
          <div class="text-start">
            <input
              class="user-input form-control text-start text-secondary bg-dark"
              type="text"
              v-model="searchName"
              placeholder="Event Name"
              minlength="6"
              maxlength="50"
              @keyup="searchEvents"
              required
            />
            <select
              class="user-input form-select text-start text-secondary bg-dark"
              @change="searchEvents"
              v-model="selectLocation"
            >
              <option class="text text-secondary" value="">Select location</option>
              <option
                class="text text-secondary"
                v-for="location in locations"
                :key="location.id"
                :value="location.id"
              >
                {{ location.name }}
              </option>
            </select>
          </div>
          <h1 class="text-success">Event List</h1>
          <div class="form-control table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Description</th>
                  <th>Lan</th>
                  <th>Location</th>
                  <th>Capacity</th>
                  <th>Spaces left</th>
                  <th>Date</th>
                  <th v-if="authService.user.value">Share</th>
                  <th>Register</th>
                </tr>
              </thead>
              <tbody class="container">
                <tr
                  v-if="events.length !== 0"
                  class="text-center"
                  v-for="event in events"
                  :key="event.id"
                  @click="searchEvents"
                >
                  <td>{{ event.name }}</td>
                  <td>{{ event.description }}</td>
                  <td>{{ event.lan ? "🟩" : "🟥" }}</td>
                  <td>{{ getLocationName(event.location) }}</td>
                  <td>{{ event.capacity }}</td>
                  <td>{{ event.capacity - event.current_capacity }}</td>
                  <td>{{ event.date }}</td>
                  <td v-if="authService.user.value">
                    <ShareNetwork
                      network="twitter"
                      :url="url"
                      :title="'New awesome event :' + event.name + ' ' + event.description"
                    >
                      <button class="btn btn-outline-secondary btn-cercle">
                        <img class="twitter-icon" src="../images/TwitterLogo.jpg" alt="Logo" />
                      </button>
                    </ShareNetwork>
                    <ShareNetwork
                      network="facebook"
                      :url="url"
                      :title="'New awesome event :' + event.name + ' ' + event.description"
                    >
                      <button class="btn btn-outline-secondary btn-cercle">
                        <img class="facebook-icon" src="../images/FacebookLogo.jpg" alt="Logo" />
                      </button>
                    </ShareNetwork>
                    <ShareNetwork
                      network="whatsapp"
                      :url="url"
                      :title="'New awesome event :' + event.name + ' ' + event.description"
                    >
                      <button class="btn btn-outline-secondary btn-cercle">
                        <img class="whatsapp-icon" src="../images/WhatsappLogo.jpg" alt="Logo" />
                      </button>
                    </ShareNetwork>
                    <ShareNetwork
                      network="linkedin"
                      :url="url"
                      :title="'New awesome event :' + event.name + ' ' + event.description"
                    >
                      <button class="btn btn-outline-secondary btn-cercle">
                        <img class="linkedin-icon" src="../images/Linkedin.jpg" alt="Logo" />
                      </button>
                    </ShareNetwork>
                  </td>
                  <td>
                    <button
                      :disabled="!isAvailable(event)"
                      class="btn btn-success"
                      @click="registerMe(event)"
                    >
                      Register
                    </button>
                  </td>
                </tr>
                <tr v-else>
                  <td class="text-center text-danger" :colspan="authService.user.value ? 9 : 8">
                    - - - - - - No events found - - - - - -
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import eventService from "@/services/eventService"
import locationService from "@/services/locationService"
import authService from "@/services/authService"
import eventRegistrationService from "@/services/eventRegistrationService"
import { ShareNetwork } from "vue-social-sharing"
import router from "@/router"

export default {
  name: "EventsView",
  data() {
    //events
    return {
      locations: [],
      url: "https://webdev-project.ch/#/events",
      events: [],
      event: {
        id: 0,
        name: "",
        description: "",
        lan: false,
        location: "",
        date: "",
        capacity: 0,
        current_capacity: 0
      },
      searchName: "",
      land: false,
      data: "",
      response: null,
      selectLocation: ""
    }
  },
  computed: {
    authService() {
      return authService
    },
    isNotEmpty() {
      return (
        this.event.name &&
        this.event.description &&
        this.event.location &&
        this.event.date &&
        this.event.capacity > 0
      )
    }
  },
  async mounted() {
    await authService.checkToken()
    eventService.getEvents().then((events) => {
      this.events = events.data
      this.selectedEvent = this.events[0]
      this.commentsId = this.events[0].id
    })
    locationService.getLocations().then((locations) => {
      this.locations = locations.data
    })
  },
  methods: {
    router() {
      return router
    },
    //register me if date is not passed and if the max number of participants is not reached
    registerMe(event) {
      if (event.date > new Date().toISOString().slice(0, 10)) {
        if (event.current_capacity < event.capacity) {
          eventRegistrationService.register(event.id).then((response) => {
            this.events = this.events.map((e) => {
              if (e.id === event.id) {
                e.current_capacity = response.data.current_capacity
              }
              return e
            })
          })
        } else {
          alert("Max number of participants reached")
        }
      } else {
        alert("Event date is passed")
      }
    },
    searchEvents() {
      eventService.findEvent(this.searchName, "", "", this.selectLocation).then((events) => {
        this.events = events.data
      })
    },
    addEvent() {
      eventService
        .addEvent(
          this.event.name,
          this.event.description,
          this.event.lan,
          this.event.location,
          this.event.date.slice(0, 10),
          this.event.capacity
        )
        .then((event) => {
          this.events.push(event.data)
          this.clearFields()
        })
    },
    clearFields() {
      this.event.name = ""
      this.event.description = ""
      this.event.land = ""
      this.event.location = ""
      this.event.date = ""
      this.$refs.name.focus()
    },
    getLocationName(locationId) {
      try {
        return this.locations.find((location) => location.id === locationId).name
      } catch (e) {
        return "null"
      }
    },
    isAvailable(event) {
      return (
        event.date > new Date().toISOString().slice(0, 10) &&
        event.current_capacity < event.capacity &&
        authService.user.value
      )
    }
  },
  components: {
    ShareNetwork
  }
}
</script>
<style scoped>
.center {
  text-align: center;
}

.user-input {
  width: 21%;
}

#root {
  margin-left: 2em;
  margin-right: 2em;
}

.text-start {
  display: flex;
  margin-bottom: 1em;
}

.text-start:first-child {
  margin-right: 1em;
}
.twitter-icon {
  width: 80%; /* Définissez la largeur de l'icône Twitter sur 100% du bouton */
  height: auto; /* Laissez 'auto' pour conserver les proportions de l'image */
}
.facebook-icon {
  width: 100%; /* Définissez la largeur de l'icône Twitter sur 100% du bouton */
  height: auto; /* Laissez 'auto' pour conserver les proportions de l'image */
}
.whatsapp-icon {
  width: 100%; /* Définissez la largeur de l'icône Twitter sur 100% du bouton */
  height: auto; /* Laissez 'auto' pour conserver les proportions de l'image */
}
.linkedin-icon {
  width: 100%; /* Définissez la largeur de l'icône Twitter sur 100% du bouton */
  height: auto; /* Laissez 'auto' pour conserver les proportions de l'image */
}
.btn-cercle {
  width: 30px;
  height: 30px;
  padding: 0;
  border: 180px;
  border-radius: 180px;
}
</style>
