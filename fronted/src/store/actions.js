import { 
  USER_LOGIN, 
  USER_LOGOUT 
} from './mutations_type'

const actions = {
  login(context, userInfo) {
    context.commit(USER_LOGIN, userInfo)
  },
  logout(context) {
    context.commit(USER_LOGOUT)
  }
}

export default actions
