import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import router from './router'
import store from './store'
import Vue3Geolocation from 'vue3-geolocation';



// import * as VueGoogleMaps from "vue2-google-maps";

import VueGoogleMaps from '@fawmi/vue-google-maps'


// import  { VueGeolocation } from 'vue-browser-geolocation';


const app = createApp(App).use(store).use(router)



app.use(Vue3Geolocation)



app.use(ElementPlus)

app.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyC9SSiHS7Va-YfYv3RojyCeVva48AHKSqQ',
    },
}).mount('#app')

