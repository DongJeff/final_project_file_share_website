<template>
  <div class="password">
    <label for="password">encrypt file:</label>
    <input 
      :type="isShow?'':'password'"
      class="common-input"
      :value="password"
      @input="$emit('input', $event.target.value)"
      @blur="checkInput"
      placeholder="Please encrypt the file"
    />
    <i class="icon"   
      :style="{
        backgroundImage:`url(${isShow?open:close})`
      }" 
      @click="isShow = !isShow"
    />
  </div>
</template>

<script>
export default {
  name: 'ExtractCode',
  model: {
    prop: 'password',
    event: 'input'
  },
  props: {
    password: String
  },
  data() {
    return {
      isShow: false,
      open: require('../assets/images/eye-open.png'),
      close: require('../assets/images/eye-close.png')
    }
  },
  methods: {
    checkInput() {
      !this.password &&
        this.$message.warning('Please encrypt the file')
    }
  }
}
</script>

<style lang="less">
.password {
  margin: 10px 0;
  input {
    margin-left: 10px;
  }
  .icon {
    display: inline-block;
    width: 20px;
    height: 20px;
    background-size: contain;
    vertical-align: middle;
    margin-left: 5px;
  }
}
</style>
