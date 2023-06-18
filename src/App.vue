<script>

import Jumbotron from './components/Jumbotron.vue';
import AppHeader from './components/AppHeader.vue';

export default {
  data() {
    return {
    };
  },
  components: { AppHeader, Jumbotron },
}

</script>

<template>
  <AppHeader></AppHeader>
  <Jumbotron></Jumbotron>
</template>

<style></style>
