<template>
  <div id="app">
    <CloudHeader />
      <div class="main">
        <router-view />
      </div>
    <CloudFooter />
  </div>
</template>

<script>
import CloudHeader from './components/header'
import CloudFooter from './components/footer'
import api from './api/index'
export default {
  name: 'App',
  components: {
    CloudHeader,
    CloudFooter
  },
  created() {
    if(localStorage.getItem('Authorization')) {
      this.axios({
        method: 'get',
        url: api.vip,
        headers: {
          'token': localStorage.getItem('Authorization')
        }
      }).then(res => {
        if(res.is_vip) {
          this.$store.dispatch('beVip')
        }
      })
    }
  }
}
</script>

<style lang="less">
.main {
  background-image: url('./assets/images/docbusBackground-cecc7ab219.jpg');
  height: calc(100vh - 80px);
  background-size: contain;
}
</style>
