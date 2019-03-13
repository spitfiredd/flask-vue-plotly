<template>
  <div id="mva">
    <WhiteNoise />
    <AutocorrPlot />
  </div>
</template>

<script>
import WhiteNoise from "./mva/whitenoise.vue";
import AutocorrPlot from "./mva/acf.vue";

export default {
  components: {
    WhiteNoise,
    AutocorrPlot
  }
}
</script>

<style>
#mva {
  width: 100%;
  height: 100%;
  position: relative;
}
</style>
