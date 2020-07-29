import { 
  USER_LOGIN, 
  USER_LOGOUT,
  USER_VIP
} from './mutations_type'

const actions = {
  login(context, userInfo) {
    context.commit(USER_LOGIN, userInfo)
  },
  logout(context) {
    context.commit(USER_LOGOUT)
  },
  beVip(context) {
    context.commit(USER_VIP)
  }
}

export default actions
