import api from "@/services/api"

export default {
  addEvent(name, description, lan, location, date, capacity) {
    return api.post("/event/", {
      name: name,
      description: description,
      lan: lan,
      location: location,
      date: date,
      capacity: capacity
    })
  },
  getEvents() {
    return api.get("/event/")
  },
  findEvent(name, lan, user, lid) {
    let body = {}

    if (name !== "") body.name = name
    if (lan !== "") body.lan = lan
    if (user !== "") body.user = user
    if (lid !== "") body.lid = lid

    return api.get("/event/", {
      params: body
    })
  }
}
