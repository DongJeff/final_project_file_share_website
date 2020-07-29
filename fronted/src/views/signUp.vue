<template>
  <div class="signUp-wrapper">
    <div class="signup-form">
      <el-form 
        label-width="150px" 
        label-position="right"
        :model="signForm"
        :rules="rules"
        ref="signUpForm"
      >
        <el-form-item label="Account:" prop="account">
          <el-input v-model="signForm.account" />
        </el-form-item>
        <el-form-item label="Password:" prop="password">
          <el-input v-model.trim="signForm.password" type="password" />
        </el-form-item>
        <el-form-item 
          label="Repeat password :" 
          prop="repeatPassword" 
          required
        >
          <el-input v-model.trim="signForm.repeatPassword" type="password" />
        </el-form-item>
        <el-form-item label="E-mail:" prop="email" required>
          <el-input v-model="signForm.email" />
        </el-form-item>
        <el-form-item>
          <el-button @click="submitForm">Sign Up</el-button>
        </el-form-item>
      </el-form>
      <div class="tip">
        By clicking “Sign up”, you agree to our <a>terms of service</a>, <a>privacy policy</a> and <a>cookie policy</a>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api/index'
export default {
  name: 'SignUp',
  beforeCreate() {
    if(this.$store.state.isLogin) {
      this.$router.push('/')
    }
  },
  data() {
    var userEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
      if (!value) {
        return callback(new Error('The mailbox cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Please enter the correct email format'))
        }
      }, 100)
    }
    var validatePass = (rule, value, callback) => {
      if(value === '') {
        callback(new Error('Please input your password again'))
      }else if(value !== this.signForm.password) {
        callback(new Error('The two passwords are not the same'))
      }else {
        callback()
      }
    }
    return {
      signForm: {
        account: '',
        password: '',
        repeatPassword: '',
        email: ''
      },
      rules: {
        account: [
          { 
            required:true, 
            message: 'Please enter your account', 
            trigger: 'blur' 
          }
        ],
        password: [
          {
            required:true, 
            message: 'Please enter your password', 
            trigger: 'blur' 
          }
        ],
        repeatPassword: [
          { validator: validatePass, trigger: 'blur' }
        ],
        email: [{validator: userEmail, trigger: 'blur'}]
      }
    }
  },
  methods: {
    submitForm() {
      this.$refs.signUpForm.validate(vaild => {
        if(vaild) {
          this.axios({
            method: 'post',
            url: api.register,
            data: {
              username: this.signForm.account,
              password: this.signForm.password
            },
            transformRequest: [
              function (data) {
                let ret = ''
                for (let it in data) {
                    ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
                }
                ret = ret.substring(0, ret.lastIndexOf('&'));
                return ret
              }
            ], 
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
          }).then(() => {
            this.$message({
              message: 'register successfully',
              type: 'success'
            })
            this.$router.push('/')
          })
        }else {
          return false
        }
      })
    }
  }
}
</script>

<style lang="less">
.signUp-wrapper {
  position: relative;
  .signup-form {
    position: absolute;
    left: 50%;
    top: 70px;
    transform: translateX(-50%);
    width: 35%;
    padding: 30px;
    box-shadow: -4px -4px 3px rgba(183,183,183,.6), 4px 4px 3px rgba(183,183,183,.6);
    border-radius: 10px;
    background-color: #ffffff;
    text-align: center;
    .el-button {
      width: 100%;
      background-color: #35AC70;
      color: #ffffff;
      font-size: 18px;
      border: none;
    }
    .tip {
      margin-top: 30px;
      text-align: left;
      font-size: 14px;
      color: #6A737C;
      line-height: 18px;
      a {
        color: #0077CC;
        cursor: pointer;
      }
    }
  }
}
</style>
