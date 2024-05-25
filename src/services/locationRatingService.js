import api from "@/services/api"

export default {
  getRating(locationId) {
    let body = {}
    if (locationId !== "") body.lid = locationId
    return api.get(`locationRating/`, {
      params: body
    })
  },

  postRating(rating, locationId) {
    return api.post(`locationRating/`, {
      rating: rating,
      location: locationId
    })
  },

  putRating(ratingId, rating, locationId) {
    return api.put(`locationRating/${ratingId}/`, {
      id: ratingId,
      rating: rating,
      location: locationId
    })
  }
}
