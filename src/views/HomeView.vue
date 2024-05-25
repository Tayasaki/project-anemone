<template>
  <div class="home">
    <CarouselVue />
    <!-- Trois columnes de texte au-dessous de carousel -->
    <div class="row text-center">
      <div class="col-lg-4">
        <img class="img-circle" src="../images/competition.jpg" />

        <h2>Competition</h2>
        <p>Shows how much talent you have</p>
        <p>
          <a class="btn btn-secondary" href="https://www.esports.ch/fr/" target="_blank"
            >View details &raquo;</a
          >
        </p>
      </div>
      <div class="col-lg-4">
        <img class="img-circle" src="../images/awards.jpg" />
        <h2>Awards</h2>
        <p>Your efforts will be rewarded with great prizes.</p>
        <p>
          <a
            class="btn btn-secondary"
            href="https://www.overgame.com/cash-prize-esport/"
            target="_blank"
            >View details &raquo;</a
          >
        </p>
      </div>
      <div class="col-lg-4">
        <img class="img-circle" src="../images/friends.jpg" />
        <h2>Make friends</h2>
        <p>Produits d'origine suisse</p>
        <p>
          <a
            class="btn btn-secondary"
            href="https://mondialdesjeux.com/esport/comment-creer-team-esport/"
            target="_blank"
            >View details &raquo;</a
          >
        </p>
      </div>
      <hr class="featurette-divider" />
      <div class="row featurette">
        <div class="col-md-7">
          <h2 class="featurette-heading">
            Registration for LAN or E-SPORTS events :
            <span class="text-muted"
              >you can register for LAN or E-SPORTS events from any digital technology.
            </span>
          </h2>
          <p class="lead">Today, you have the technologies at your fingertips.</p>
        </div>
        <div class="col-md-5">
          <img
            id="img1"
            class="rounded mx-auto d-block"
            alt="image4"
            src="https://binaryinformatics.com/wp-content/uploads/2018/10/mobile-application.jpg"
          />
        </div>
      </div>
      <hr class="featurette-divider" />

      <div class="row featurette">
        <div class="col-md-7 order-md-2">
          <h2 class="featurette-heading">
            To rate and comment on our events :
            <span class="text-muted"
              >You can rate and comment on our events to have better experiences in the
              future.</span
            >
          </h2>
          <p class="lead">
            This can be useful for those who want to know what others think of the events they are
          </p>
        </div>
        <div class="col-md-5 order-md-1">
          <img
            class="rounded mx-auto d-block"
            alt="image5"
            id="img1"
            src="https://static.vecteezy.com/ti/vecteur-libre/p2/2756521-notation-etoiles-jaunes-gratuit-vectoriel.jpg"
          />
        </div>
      </div>
      <hr class="featurette-divider" />

      <div class="row featurette">
        <div class="col-md-7">
          <h2 class="featurette-heading">
            LAN-SPORT :
            <span class="text-muted">
              short for Local Area Network sport, is a type of video game competition where players
              connect their computers or consoles to a local network, typically in the same physical
              location, and compete against each other in real-time. LAN events can range from small
              gatherings with friends to large-scale tournaments with professional players, big
              prize pools, and a live audience.</span
            >
          </h2>
          <p class="lead">
            Unlike online gaming, where players connect to the internet to compete against each
            other remotely, LAN gaming allows for lower latency, which means less delay or lag
            between player actions and game responses. This can make for a smoother and more
            enjoyable gaming experience.
          </p>
        </div>
        <div class="col-md-5">
          <img
            id="img1"
            class="rounded mx-auto d-block"
            alt="image4"
            src="https://i.pinimg.com/originals/1a/3f/a3/1a3fa30e2a37723ad22da726f81a51f3.jpg"
          />
        </div>
      </div>
      <hr class="featurette-divider" />

      <div class="row featurette">
        <div class="col-md-7 order-md-2">
          <h2 class="featurette-heading">
            E-SPORT :
            <span class="text-muted">
              short for electronic sport, is a form of competitive video gaming. In e-sports,
              professional players or teams compete against each other in multiplayer video games,
              often in organized tournaments or leagues with large audiences and substantial prize
              pools.</span
            >
          </h2>
          <p class="lead">
            Popular e-sports games include League of Legends, Dota 2, Fortnite, Counter-Strike:
            Global Offensive, and many others.
          </p>
        </div>
        <div class="col-md-5 order-md-1">
          <img
            class="rounded mx-auto d-block"
            alt="image5"
            id="img1"
            src="https://www.journaltranscript.com/wp-content/uploads/2020/08/esports.jpg"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import CarouselVue from "../components/CarouselVue.vue"
import authService from "@/services/authService"

export default {
  components: {
    CarouselVue
  },
  async mounted() {
    await authService.checkToken()
  }
}
</script>
<style scoped>
#img {
  max-width: 1800px;
  max-height: 800px;
  filter: brightness(0.9);
}
#img1 {
  max-width: 500px;
  max-height: 500px;
}
.img-circle {
  width: 140px;
  height: 140px;
  border: 180px;
  border-radius: 180px;
}

.row {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
