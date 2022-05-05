import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
// import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'leaflet/dist/leaflet.css'


// createApp(App).use(router).mount('#app')
// const app = createApp(App).mount('#app');
// App.use(BootstrapVue)
const app = createApp(App);
app.use(router);
app.mount('#app')



