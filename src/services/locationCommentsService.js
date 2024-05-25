import api from "@/services/api"

/**
 * This is the service module for location comments.<br/>
 * It is responsible for all communication with the backend regarding location comments.<br/>
 * It is advised to always use strings for all parameters.<br/>
 */
export default {
  getAllComments() {
    return api.get(`locationComment/`)
  },
  getComments(locationId) {
    return api.get(`locationComment/?lid=${locationId}`)
  },
  findComments(locationId, user) {
    let body = {}
    if (locationId !== "") body.lid = locationId
    if (user !== "") body.user = user
    return api.get(`locationComment/`, {
      params: body
    })
  },

  postComment(comment, locationId) {
    return api.post(`locationComment/`, {
      comment: comment,
      location: locationId
    })
  },

  editComment(commentId, comment, locationId) {
    return api.put(`locationComment/${commentId}/`, {
      id: commentId,
      comment: comment,
      location: locationId
    })
  },

  deleteComment(commentId) {
    return api.delete(`locationComment/${commentId}/`)
  }
}
