<template>
  <div class="flex">
    <div class="side">
      <p id="title">Locations</p>
      <form>
        <div class="row">
          <div class="col">
            <input class="form-control" type="text" placeholder="Name" v-model="searchName" />
          </div>
          <div class="col">
            <input class="form-control" type="text" placeholder="Zip" v-model="searchZip" />
          </div>
          <div class="col">
            <button class="custom-button" @click="searchLocation">Search</button>
          </div>
        </div>
      </form>
      <form v-if="authService.user.value">
        <div class="row">
          <div class="col">
            <input class="form-control" type="text" placeholder="Name" v-model="location.name" />
          </div>
          <div class="col">
            <input class="form-control" type="text" placeholder="Zip" v-model="location.zip" />
          </div>
          <div class="col">
            <button class="custom-button" @click="addLocation">Add</button>
          </div>
        </div>
      </form>
      <div
        class="menu-item"
        v-for="location in locations"
        :key="location.id"
        @click="selectLocation(location)"
      >
        <p class="name">{{ location.name }}</p>
      </div>
    </div>
    <div class="content">
      <LocationDisplay :location="selectedLocation" />
      <LocationComments :location-id="commentsId" :location="selectedLocation" />
    </div>
  </div>
</template>
<script>
import locationService from "@/services/locationService"
import LocationComments from "@/components/LocationComments.vue"
import LocationDisplay from "@/components/LocationDisplay.vue"
import authService from "@/services/authService"

export default {
  name: "LocationsView",
  components: { LocationDisplay, LocationComments },
  data() {
    return {
      searchName: "",
      searchZip: "",
      response: null,
      data: null,

      selectedLocation: null,
      commentsId: -1,

      locations: [],
      location: {
        id: 0,
        name: "",
        zip: ""
      }
    }
  },
  async mounted() {
    await authService.checkToken()
    this.locations = locationService.getLocations().then((locations) => {
      this.locations = locations.data
      this.selectedLocation = locations.data[0]
      this.commentsId = locations.data[0].id
    })
  },
  computed: {
    authService() {
      return authService
    }
  },
  methods: {
    addLocation() {
      locationService
        .addLocation(this.location.name, this.location.zip)
        .then((response) => {
          this.response = response
          this.data = response.data
        })
        .catch((error) => {
          this.response = error.response
          this.data = error.response.data
        })
        .finally(() => {
          locationService.getLocations().then((locations) => {
            this.locations = locations.data
          })
        })
    },
    searchLocation() {
      locationService.findLocation(this.searchName, this.searchZip).then((response) => {
        this.locations = response.data
      })
    },
    selectLocation(location) {
      this.selectedLocation = location
      this.commentsId = location.id
    },
    updateLocation(locationId) {
      let index = this.locations.findIndex((location) => location.id === locationId)
      locationService.getLocation(locationId).then((response) => {
        this.locations[index] = response.data
        this.selectedLocation = response.data
      })
    }
  }
}
</script>

<style scoped>
.flex {
  display: flex;
  flex-direction: row;
  margin-left: 2em;
}

.side {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;

  width: 20%;
  padding-top: 1em;
}

.content {
  width: 80%;
  margin-left: 2em;
  margin-right: 2em;
  margin-top: 1em;
}

#title {
  font-size: 20px;
  font-weight: bold;
  color: black;
}

.menu-item {
  color: black;
  cursor: pointer;
}

.menu-item:hover {
  background-color: #d7317c;
  color: white;
}

.name {
  font-size: 16px;
  font-weight: bold;
  margin: 0;
  padding: 1em;
}

input,
button {
  max-height: 2em;
}

.col {
  padding: 5px;
}

.custom-button {
  background-color: #e83283;
  border: none;
  border-radius: 10px;
  width: 100%;
  height: 2em;
}
</style>
