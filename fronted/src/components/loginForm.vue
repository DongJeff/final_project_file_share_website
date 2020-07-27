<template>
  <div class="common-box loginForm">
    <h2>Log in</h2>
    <el-form 
      :model="form"
      label-position="left" 
      label-width="80px"
    >
      <el-form-item label="Account:">
        <el-input v-model="form.account" />
      </el-form-item>
      <el-form-item label="Password:">
        <el-input 
          v-model="form.password" 
          type="password"
        />
      </el-form-item>
    </el-form>
    <div class="helps">
      <span>Forget password?</span>
      <span @click="SignUpClickHandler">Sign up</span>
    </div>
    <el-button 
      width="200px"
      @click="loginHandler"
    >
      Log in
    </el-button>
  </div>
</template>

<script>
import api from '../api/index'
export default {
  name: 'LoginForm',
  data() {
    return {
      form: {
        account: '',
        password: ''
      }
    }
  },
  methods: {
    SignUpClickHandler() {
      this.$router.push({ path: 'signup' })
    },
    loginHandler() {
      if(this.form.account && this.form.password) {
        this.login()
      }else {
        this.$message({
          message: 'Please complete the login information',
          type: 'info'
        })
      }
    },
    login() {
      this.axios(api.login, this.form)
      .then(res => {
        this.$store.dispatch('login', {
          account: res.account,
          token: 'Bearer ' + res.token
        })
        this.$message({
          message: 'log in successfully',
          type: 'success'
        })
      })
      .catch(() => {
        this.$message({
          message: 'wrong account or password',
          type: 'error'
        })
      })
    }
  }
}
</script>

<style lang="less">
.loginForm {
  width: 80%;
  margin: 20px auto;
  h2 {
    color: #333333;
    font-size: 25px;
    margin-bottom: 20px;
  }
  .helps {
    color: #606266;
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    cursor: pointer;
  }
  .el-button {
    margin-top: 20px;
    width: 60%;
    background-color: #35AC70;
    color: #ffffff;
    font-size: 18px;
  }
}
</style>
