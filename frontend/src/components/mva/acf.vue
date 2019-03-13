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
      layout: { title: "AR(1) Time Series on white noise, phi=.9" },
      options: {}
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/api/v1/mva")
      .then(response => {
        this.data = response.data.autocorr;
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  }
};
</script>