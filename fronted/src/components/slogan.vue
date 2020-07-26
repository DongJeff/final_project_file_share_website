<template>
  <p 
    class="slogan" 
    :style="{ fontSize: fontSize + 'px',lineHeight: lineHeight }"
  >
    告别公共电脑u盘中毒
    <br>
    防止账号被盗
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
