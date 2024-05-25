<template>
  <div class="container">
    <h1 class="mt-5 text-success">Your Event Registrations</h1>
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
        </tr>
      </thead>
      <tbody class="container">
        <tr
          v-if="registeredEvents.length !== 0"
          class="text-center"
          v-for="event in registeredEvents"
          :key="event.id"
        >
          <td>{{ event.name }}</td>
          <td>{{ event.description }}</td>
          <td>{{ event.lan ? "🟩" : "🟥" }}</td>
          <td>{{ getLocationName(event.location) }}</td>
          <td>{{ event.capacity }}</td>
          <td>{{ event.capacity - event.current_capacity }}</td>
          <td>{{ event.date }}</td>
        </tr>
        <tr v-else>
          <td class="text-center text-danger" colspan="8">
            - - - - - - No events found - - - - - -
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import eventService from "@/services/eventService"
import locationService from "@/services/locationService"
import eventRegistrationService from "@/services/eventRegistrationService"
import authService from "@/services/authService"

export default {
  name: "EventRegistration",
  data() {
    return {
      events: [],
      locations: [],
      registrations: [],
      registeredEvents: []
    }
  },
  computed: {
    authService() {
      return authService
    }
  },
  methods: {
    getEvent(eventId) {
      let event = this.events.filter((event) => {
        return event.id === eventId
      })

      if (event.length > 0) return event[0]
      return null
    },
    getLocationName(locationId) {
      let location = this.locations.filter((location) => {
        return location.id === locationId
      })

      if (location.length > 0) return location[0].name
      return ""
    }
  },
  async mounted() {
    await authService.checkToken()
    if (!authService.user.value) return

    await eventService.getEvents().then((events) => {
      this.events = events.data
    })
    await locationService.getLocations().then((locations) => {
      this.locations = locations.data
    })
    await eventRegistrationService
      .filterRegistrations("", authService.user.value.username)
      .then((registrations) => {
        this.registrations = registrations.data

        this.registrations.forEach((registration) => {
          this.registeredEvents.push(this.getEvent(registration.event))
        })
      })
  }
}
</script>

<style scoped></style>
