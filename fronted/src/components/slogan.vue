<template>
  <p 
    class="slogan" 
    :style="{ fontSize: fontSize + 'px',lineHeight: lineHeight }"
  >
    Farewell to public computer U disk poisoning
    <br>
    Prevent account theft
  </p>
</template>

<script>
export default {
  name: 'Slogan',
  props: {
    fontSize: {
      type: Number,
      default: 26
    }
  },
  computed: {
    lineHeight() {
      return this.fontSize + 5 + 'px'
    }
  }
}
</script>

<style lang="less">
.slogan {
  text-align: center;
  color: #35AC70;
  font-size: 26px;
  font-weight: 700;
  line-height: 30px;
}
</style>
