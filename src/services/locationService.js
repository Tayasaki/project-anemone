import api from "@/services/api"

export default {
  addLocation(name, zip) {
    return api.post("/location/", {
      name: name,
      zip: zip
    })
  },
  getLocations() {
    return api.get("location/")
  },
  getLocation(id) {
    return api.get(`location/${id}`)
  },
  updateLocation(id, name, zip) {
    return api.put(`/location/${id}`, {
      name: name,
      zip: zip
    })
  },
  deleteLocation(id) {
    return api.delete(`/location/${id}`)
  },
  findLocation(name, zip) {
    let body = {}
    if (name !== "") body.name = name
    if (zip !== "") body.zip = zip
    return api.get("/location/", {
      params: body
    })
  }
}
