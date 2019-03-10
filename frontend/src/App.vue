<template>
  <div id="app">
    <HelloPlotly />
  </div>
</template>

<script>
import HelloPlotly from "./components/HelloPlotly.vue";

export default {
  name: "app",
  components: {
    HelloPlotly
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
