import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import router from './router'
import store from './store'


const app = createApp(App).use(store).use(router)

app.use(ElementPlus)
app.mount('#app')
