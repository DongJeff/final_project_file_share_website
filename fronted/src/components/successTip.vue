<template>
  <div class="success-wrapper">
    <div class="tip-card">
      <div class="tip-title">
        <span>Upload successfully</span>
        <span title="close tips">x</span>
      </div>
      <div class="upload-info">
        <p>24小时内在提取页面下载</p>
        <p>提取方式一:</p>
        <p>凭文件名:Internet Download Manager Crack.exe提取</p>
        <p>提取方式二:</p>
        <p>凭提取码:<span class="highlight">st8fgu</span>提取</p>
      </div>
      <div class="sure" @click="$emit('close')">OK</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SuccessTip'
}
</script>

<style lang="less">
.success-wrapper {
  text-align: left;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: rgba(0, 0, 0, .3);
  z-index: 9;
  .tip-card {
    background-color: #fff;
    width: 35%;
    margin: 80px auto;
    border-radius: 3px;
    .tip-title {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #eeeeee;
      padding-bottom: 10px;
      padding: 20px;
      span {
        &:first-child {
          font-size: 20px;
          font-weight: bolder;
        }
        &:last-child {
          font-size: 18px;
          cursor: pointer;
        }
      }
    }
    .upload-info {
      font-size: 14px;
      padding: 10px 20px;
      p {
        line-height: 18px;
      }
      .highlight {
        color: #0D16CA;
      }
    }
    .sure {
      text-align: right;
      padding: 15px;
      color: #3593D2;
      cursor: pointer;
    }
  }
}
</style>
