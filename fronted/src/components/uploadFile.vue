<template>
  <div class="common-box upload-wrapper">
    <h2>Upload your files</h2>
      <span class="methods-tips">
        method:
      </span>
      <el-radio-group v-model="method">
        <el-radio :label="0">public</el-radio>
        <el-radio :label="1">private</el-radio>
      </el-radio-group>
      <extract-code v-if="method === 1" v-model="password"/>
    <el-upload
      ref="upload"
      drag
      :limit="1"
      action="https://jsonplaceholder.typicode.com/posts/"
      :file-list="fileList"
      auto-upload
      :on-success="successHandler"
      :on-error="errorHandler"
      :disabled="isBanSubmit"
    >
      <i class="el-icon-upload" />
      <div class="el-upload__text">
        Drag your file here or <em>click to upload</em>
      </div>
      <div class="el-upload__tip" slot="tip">
        Tips: files should be less than 10MB & files will be kept for 24h
      </div>
    </el-upload>
    <SuccessTip 
      v-if="iShowSuccessTips"
      @close="closeHandler"
    />
  </div>
</template>

<script>
import ExtractCode from '../components/extractCode'
import SuccessTip from '../components/successTip'
export default {
  name: 'UploadFile',
  components: {
    ExtractCode,
    SuccessTip
  },
  data() {
    return {
      method: 0,
      fileList: [],
      password: '',
      iShowSuccessTips: false
    }
  },
  methods: {
    successHandler() {
      this.iShowSuccessTips = true
    },
    errorHandler() {
      this.$message({
        message: 'upload failed',
        type: 'error'
      })
    },
    closeHandler() {
      this.iShowSuccessTips = false
    }
  },
  computed: {
    isBanSubmit() {
      return this.method === 1 && !this.password
    }
  }
}
</script>

<style lang="less">
.upload-wrapper {
  margin-top: 20px;
  .methods-tips {
    margin-right: 10px;
  }
  h2 {
    color: #333333;
    font-size: 30px;
    padding-bottom: 10px;
  }
  .el-upload-dragger {
    margin-top: 10px;
  }
}
</style>
