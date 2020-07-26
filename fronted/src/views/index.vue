<template>
  <div class="index-wrapper">
    <div class="container">
      <h1 class="title">Cloud Document</h1>
      <div class="main-body">
        <swiper />
        <div class="files-area">
          <slogan :font-size="20"/>
          <FileBox v-if="isLogin" />
          <LoginForm v-else/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FileBox from '../components/uploadFile'
import Swiper from '../components/swiper'
import Slogan from '../components/slogan'
import LoginForm from '../components/loginForm'
import { mapState } from 'vuex'
export default {
  name: 'Index',
  components: {
    Swiper,
    FileBox,
    Slogan,
    LoginForm,
  },
  computed: {
    ...mapState(['isLogin'])
  }
}
</script>

<style lang="less">
.index-wrapper {
  .title {
    color: #333333;
    font-size: 30px;
    padding-top: 20px;
  }
  .main-body {
    display: flex;
    .files-area {
      width: 40%;
      margin: 0 auto;
    }
  }
}
</style>
