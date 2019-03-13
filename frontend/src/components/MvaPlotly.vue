<template>
  <div>
    <MvaPlot />
    <AutocorrPlot />
  </div>
</template>

<script>
import MvaPlot from "./mva/mva.vue";
import AutocorrPlot from "./mva/acf.vue";

export default {
  components: {
    MvaPlot,
    AutocorrPlot
  }
}
</script>