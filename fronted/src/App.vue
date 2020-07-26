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
export default {
  name: 'App',
  components: {
    CloudHeader,
    CloudFooter
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
