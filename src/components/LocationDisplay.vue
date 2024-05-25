<template>
  <div v-if="location !== null">
    <div class="location-display">
      <div class="location-display-header">
        <h1>{{ location.name }}</h1>
        <div id="rating">
          <img
            class="star"
            v-bind:src="stars[0]"
            @mouseover="setStartImages(1)"
            @mouseleave="setStartImages(this.location.rating)"
            @click="sendRating(1)"
            alt="star1"
          />
          <img
            class="star"
            v-bind:src="stars[1]"
            @mouseover="setStartImages(2)"
            @mouseleave="setStartImages(this.location.rating)"
            @click="sendRating(2)"
            alt="star2"
          />
          <img
            class="star"
            v-bind:src="stars[2]"
            @mouseover="setStartImages(3)"
            @mouseleave="setStartImages(this.location.rating)"
            @click="sendRating(3)"
            alt="star3"
          />
          <img
            class="star"
            v-bind:src="stars[3]"
            @mouseover="setStartImages(4)"
            @mouseleave="setStartImages(this.location.rating)"
            @click="sendRating(4)"
            alt="star4"
          />
          <img
            class="star"
            v-bind:src="stars[4]"
            @mouseover="setStartImages(5)"
            @mouseleave="setStartImages(this.location.rating)"
            @click="sendRating(5)"
            alt="star5"
          />
        </div>
      </div>
      <div class="location-display-body">
        <p>Name: {{ location.name }}</p>
        <p>Zip: {{ location.zip }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import locationRatingService from "@/services/locationRatingService"
import fullStar from "@/images/rating/full.png"
import halfStar from "@/images/rating/half.png"
import emptyStar from "@/images/rating/empty.png"

export default {
  name: "LocationDisplay",
  props: {
    location: {
      required: true
    }
  },
  data() {
    return {
      stars: ["", "", "", "", ""]
    }
  },
  methods: {
    setStartImages(rating) {
      for (let i = 0; i < 5; i++) {
        this.stars[i] = emptyStar
      }

      if (rating === "0" || rating === 0) return

      let full = rating - (rating % 1)
      let half = rating % 1
      let empty = 5 - full - half

      for (let i = 0; i < full; i++) {
        this.stars[i] = fullStar
      }

      if (half > 0) {
        this.stars[full] = halfStar
      }

      for (let i = full + 1; i < full + 1 + empty; i++) {
        this.stars[i] = emptyStar
      }
    },
    sendRating(rating) {
      locationRatingService.getRating(this.location.id).then((response) => {
        if (!Object.keys(response.data).length) {
          locationRatingService
            .postRating(rating, this.location.id)
            .then(() => this.$parent.updateLocation(this.location.id))
        } else {
          locationRatingService
            .putRating(response.data[0].id, rating, this.location.id)
            .then(() => this.$parent.updateLocation(this.location.id))
        }
      })
    }
  },
  watch: {
    location() {
      this.setStartImages(this.location.rating)
    }
  }
}
</script>

<style scoped>
#rating {
  display: flex;
}

.star {
  height: 2em;
  padding-left: 10px;
}

.location-display {
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px;
}

.location-display-header {
  display: flex;
  justify-content: space-between;
}

.location-display-body {
  display: flex;
  justify-content: space-between;
}

.location-display-body p {
  margin: 0;
}

.location-display-body p:first-child {
  margin-right: 10px;
}

.location-display-body p:last-child {
  margin-left: 10px;
}
</style>
