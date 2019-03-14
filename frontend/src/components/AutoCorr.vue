<template>
  <vue-plotly :data="data" :layout="layout" :options="options" />
</template>

<script>
import VuePlotly from "@statnett/vue-plotly";
import axios from "axios";

export default {
  components: {
    VuePlotly
  },
  data() {
    return {
      data: null,
      layout: null,
      options: {}
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/api/v1/mva")
      .then(response => {
        this.data = response.data;
        this.layout = response.layout;
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  }
};
</script>
