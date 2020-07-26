import Vue from 'vue'
import App from './App.vue'
import router from './routes'
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from './store/index'
import './assets/css/reset.css'
import './assets/css/common.less'

const isMock = true

if(isMock) {
  require('./mock/index')
}

import { 
  Upload, 
  Radio, 
  RadioGroup,
  Button,
  Form,
  FormItem,
  Input,
  Select,
  Option,
  Message,
  MessageBox
} from 'element-ui'

Vue.use(Upload)
Vue.use(Radio)
Vue.use(RadioGroup)
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Select)
Vue.use(Option)

axios.defaults.baseURL = '/api'
axios.defaults.timeout = 8000

axios.interceptors.response.use(response => {
  let res = response.data
  if(res.status === 0) {
    return res.data
  }else if(res.status === 10) {
    window.location.href = '/#/'
    return Promise.reject(res)
  }else {
    return Promise.reject(res)
  }
}, error => {
  let res = error.response
  Message({
    message: res.msg,
    type: 'error'
  })
  return Promise.reject(error)
})

Vue.use(VueAxios, axios)

Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
