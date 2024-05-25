import api from "@/services/api"

export default {
  register(eventId) {
    return api.post("/eventRegistration/", {
      event: eventId
    })
  },

  getRegistrations() {
    return api.get("/eventRegistration/")
  },

  filterRegistrations(eid, user) {
    let body = {}
    if (eid !== "") body.event = eid
    if (user !== "") body.user = user
    return api.get("/eventRegistration/", {
      params: body
    })
  }
}
