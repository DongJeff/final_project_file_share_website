import { 
  USER_LOGIN, 
  USER_LOGOUT,
  USER_VIP
} from './mutations_type'

const mutations = {
  [USER_LOGIN](state, userInfo) {
    state.isLogin = true
    state.account = userInfo.account
    state.Authorization = userInfo.token
    localStorage.setItem('cloudUser', userInfo.account)
    localStorage.setItem('Authorization', userInfo.token)
  },
  [USER_LOGOUT](state) {
    state.isLogin = false
    state.account = ''
    state.Authorization = ''
    localStorage.removeItem('cloudUser')
    localStorage.removeItem('Authorization')
  },
  [USER_VIP](state) {
    state.isVip = true
  }
}

export default mutations
