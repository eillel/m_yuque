import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import 'font-awesome/css/font-awesome.css'
import 'normalize.css'
import './assets/css/base.css'
Vue.config.productionTip = false
Vue.prototype.$bus = new Vue()
Vue.use(ViewUI);


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
