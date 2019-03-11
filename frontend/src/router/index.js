import Vue from "vue";
import Router from "vue-router";
import HelloPlotly from "@/components/HelloPlotly.vue";
import Home from "@/components/Home.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/plot",
      name: "HelloPlotly",
      component: HelloPlotly
    }
  ]
});
