import { createStore } from 'vuex'
import ModuleUser from './user.js'
import ModuleWeather from './weather.js'


export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    user: ModuleUser,
    weather: ModuleWeather,
  }
});


