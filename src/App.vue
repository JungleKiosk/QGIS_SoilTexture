<script>

import { links } from './data/linkVideo.js';

import Jumbotron from './components/Jumbotron.vue';
import AppHeader from './components/AppHeader.vue';
import BannerCards from './components/BannerCards.vue';
import SoilTexture from './components/SoilTexture.vue';
import UsdaTriangle from './components/UsdaTriangle.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  data() {
    return {
    };
  },
  components: { AppHeader, Jumbotron, BannerCards, SoilTexture, UsdaTriangle, AppFooter },
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
  <SoilTexture></SoilTexture>
  <UsdaTriangle></UsdaTriangle>
  <AppFooter></AppFooter>
</template>

<style></style>
