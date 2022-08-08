import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import router from './router'
import store from './store'
import Vue3Geolocation from 'vue3-geolocation';

import Dropdown from 'vue-simple-search-dropdown'

import VueGoogleMaps from '@fawmi/vue-google-maps'

const app = createApp(App).use(store).use(router)

app.use(Dropdown);

app.use(Vue3Geolocation)

app.use(ElementPlus)

app.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyC9SSiHS7Va-YfYv3RojyCeVva48AHKSqQ',
        libraries: "places"
    },
}).mount('#app')

