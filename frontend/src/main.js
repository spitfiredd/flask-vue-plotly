import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import SuiVue from 'semantic-ui-vue';


Vue.config.productionTip = false;
Vue.use(SuiVue);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
