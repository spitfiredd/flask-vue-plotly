import Vue from "vue";
import Vuex from "vuex";

import { sinWaves } from "@/api";

Vue.use(Vuex);

const state = {

};

const mutations = {
  setSinData(state, payload) {
    state.sinData = payload.sinData;
  }
}

const actions = {
  getSinData(context, options) {
    context.commit("setSinData", { options });
    return sinWaves(options)
  }
}

const getters = {
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
});

export default store;