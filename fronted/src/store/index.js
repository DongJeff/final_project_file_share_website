import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './actions'

Vue.use(Vuex)

const state = {
  isLogin: localStorage.getItem('Authorization') ? true : false,
  account: localStorage.getItem('cloudUser') || '' ,
  Authorization: localStorage.getItem('Authorization') || '',
  isVip: false
}

const store = new Vuex.Store({
  state,
  mutations,
  actions
})

export default store
