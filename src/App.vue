<script>

import { links } from './data/linkVideo.js';

import Jumbotron from './components/Jumbotron.vue';
import AppHeader from './components/AppHeader.vue';
import BannerCards from './components/BannerCards.vue';

export default {
  data() {
    return {
    };
  },
  components: { AppHeader, Jumbotron, BannerCards },
  computed: {
    linksData() {
      return links;
    }
  }
}

</script>

<template>
  <AppHeader></AppHeader>
  <Jumbotron></Jumbotron>
  <BannerCards :links="linksData"></BannerCards>
</template>

<style></style>
