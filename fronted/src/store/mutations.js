import { 
  USER_LOGIN, 
  USER_LOGOUT 
} from './mutations_type'

const mutations = {
  [USER_LOGIN](state, userInfo) {
    state.isLogin = true
    state.account = userInfo.account
    state.Authorization = userInfo.Authorization
    localStorage.setItem('Authorization', userInfo.Authorization)
  },
  [USER_LOGOUT](state) {
    state.isLogin = false
    state.account = ''
  }
}

export default mutations
