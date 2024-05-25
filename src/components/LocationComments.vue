<template>
  <div v-if="locationId !== -1">
    <div class="d-flex flex-start mb-2 mt-2" v-if="authService.user.value">
      <div class="card w-100">
        <div class="card-body">
          <div>
            <h5>Add a new comment</h5>
            <input v-model="newCommentText" type="text" />
            <div class="d-flex justify-content-end">
              <button @click="addComment" class="btn btn-primary btn-sm">Add</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="d-flex flex-start mb-2 mt-2" v-for="comment in comments" :key="comment.id">
      <div class="card w-100">
        <div class="card-body">
          <div>
            <h5>{{ comment.user }}</h5>
            <p v-if="comment.id !== editId">
              {{ comment.comment }}
            </p>
            <input v-else v-model="editText" type="text" />
            <div v-if="authService.user.value">
              <ShareNetwork
                network="twitter"
                :title="comment.user + ' says: ' + comment.comment + ' - (' + location.name + ')'"
                :url="url"
              >
                <button class="btn btn-outline-secondary btn-circle">
                  <img class="twitter-icon" src="../images/TwitterLogo.jpg" alt="Logo" />
                </button>
              </ShareNetwork>
              <ShareNetwork
                network="facebook"
                :title="comment.user + ' says: ' + comment.comment + ' - (' + location.name + ')'"
                :url="url"
              >
                <button class="btn btn-outline-secondary btn-circle">
                  <img class="facebook-icon" src="../images/FacebookLogo.jpg" alt="Logo" />
                </button>
              </ShareNetwork>
              <ShareNetwork
                network="whatsapp"
                :title="comment.user + ' says: ' + comment.comment + ' - (' + location.name + ')'"
                :url="url"
              >
                <button class="btn btn-outline-secondary btn-circle">
                  <img class="whatsapp-icon" src="../images/WhatsappLogo.jpg" alt="Logo" />
                </button>
              </ShareNetwork>
              <ShareNetwork
                network="linkedin"
                :title="comment.user + ' says: ' + comment.comment + ' - (' + location.name + ')'"
                :url="url"
              >
                <button class="btn btn-outline-secondary btn-circle">
                  <img class="linkedin-icon" src="../images/Linkedin.jpg" alt="Logo" />
                </button>
              </ShareNetwork>
            </div>
            <div v-if="getUser() === comment.user" class="d-flex justify-content-end">
              <button
                v-if="editId === -1 || editId !== comment.id"
                @click="deleteComment(comment.id)"
                class="delete btn btn-primary btn-sm"
              >
                Delete
              </button>
              <button
                v-if="editId === -1 || editId !== comment.id"
                @click="edit(comment.id)"
                class="btn btn-primary btn-sm"
              >
                Edit
              </button>

              <button v-if="editId === comment.id" @click="save" class="btn btn-primary btn-sm">
                Save
              </button>
              <button
                v-if="editId === comment.id"
                @click="cancel"
                class="cancel btn btn-primary btn-sm"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import locationCommentsService from "@/services/locationCommentsService"
import authService from "@/services/authService"
import { ShareNetwork } from "vue-social-sharing"
import locationService from "@/services/locationService"

export default {
  name: "LocationComments",
  computed: {
    locationService() {
      return locationService
    },
    authService() {
      return authService
    }
  },
  props: {
    locationId: {
      type: Number,
      required: true
    },
    location: {
      required: true
    }
  },
  data() {
    return {
      comments: [],
      editId: -1,
      editText: "",
      url: "https://webdev-project.ch/#/locations",

      newCommentText: ""
    }
  },
  methods: {
    edit(commentId) {
      let comment = this.comments.find((comment) => comment.id === commentId)

      this.editId = commentId
      this.editText = comment.comment
    },
    save() {
      locationCommentsService.editComment(this.editId, this.editText, this.locationId).then(() => {
        this.editId = -1
        this.editText = ""
        locationCommentsService.getComments(this.locationId).then((comments) => {
          this.comments = comments.data
        })
      })
      this.cancel()
    },
    cancel() {
      this.editId = -1
      this.editText = ""
    },
    addComment() {
      locationCommentsService.postComment(this.newCommentText, this.locationId).then(() => {
        this.newCommentText = ""
        locationCommentsService.getComments(this.locationId).then((comments) => {
          this.comments = comments.data
        })
      })
    },
    deleteComment(commentId) {
      locationCommentsService.deleteComment(commentId).then(() => {
        let comment = this.comments.findIndex((comment) => comment.id === commentId)
        this.comments.splice(comment, 1)
      })
    },
    getUser() {
      if (this.authService.user.value) {
        return this.authService.user.value.username
      }
      return null
    }
  },
  watch: {
    locationId: {
      handler: function (newLocationId) {
        locationCommentsService.getComments(newLocationId).then((comments) => {
          this.comments = comments.data
        })
      }
    }
  },
  components: {
    ShareNetwork
  }
}
</script>

<style scoped>
* {
  color: black;
}

input {
  width: 100%;
  border: none;
  border-bottom: 1px solid black;
  background-color: transparent;
  margin-bottom: 1em;
}

.cancel {
  margin-left: 1em;
}

.delete {
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

.btn-circle {
  width: 30px;
  height: 30px;
  padding: 0;
  border: 180px;
  border-radius: 180px;
}
</style>
