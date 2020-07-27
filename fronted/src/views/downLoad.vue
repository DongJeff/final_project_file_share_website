<template>
  <div class="download-wrapper">
    <div class="download">
      <slogan :font-size="18"/>
      <div class="common-box">
        <p class="download-slogan">Download your document</p>
        <div class="extract-box">
          <div v-if="isByKey">
            <p class="download-tip">
              Please enter after the upload is successful key generated for each file
            </p>
            <div class="extract-method">
              <label for="way">key:</label>
              <input 
                class="common-input" 
                id="way" 
                v-model="key"
              />
              <span class="extract">
                extract
              </span>
            </div>
          </div>
          <div v-else>
            <p class="download-tip">
              Pay attention to the special symbols that distinguish the Chinese and English input methods You need to enter the file suffix to extract correctly
            </p>
            <div class="extract-method">
              <label for="way">fileName:</label>
              <input 
                class="common-input" 
                v-model="fileName"
                id="way" 
              />
              <span class="dot">.</span>
              <el-select 
                v-model="fileExtend" 
                size="mini" 
                placeholder="file ext"
              >
                <el-option
                  v-for="item in extendNames"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
                <div class="other">
                  <label for="other-ext">other:</label>
                  <input 
                    id="other-ext"
                    v-model="fileExtend"
                  />
                </div>
              </el-select>
            </div>
            <extract-code 
              v-model="password" 
              v-if="fileType === 'private'"
            />
            <div class="file-type">
              <span style="marginRight:10px">
                file type:
              </span>
              <el-radio-group v-model="fileType">
                <el-radio label="public">public file</el-radio>
                <el-radio label="private">private file</el-radio>
              </el-radio-group>
            </div>
            <div 
              class="extract-button"
              :class="{ active: cloudExtract }"
            >
              Extract
            </div>
          </div>
        </div>
        <div class="use-file-name extract" @click="isByKey = !isByKey">
          Extract by file name
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Slogan from '../components/slogan'
import ExtractCode from '../components/extractCode'
export default {
  name: 'DownLoad',
  components: {
    Slogan,
    ExtractCode
  },
  data() {
    return {
      isByKey: true,
      fileName: '',
      key: '',
      fileType: 'public',
      extendNames: [
        {
          value: '0',
          label: 'docx'
        },
        {
          value: '1',
          label: 'doc'
        },
        {
          value: '2',
          label: 'pdf'
        },
        {
          value: '3',
          label: 'xls'
        },
        {
          value: '4',
          label: 'ppt'
        },
        {
          value: '5',
          label: 'ppt'
        },
        {
          value: '6',
          label: 'pptx'
        },
        {
          value: '7',
          label: 'jpg'
        },
        {
          value: '8',
          label: 'png'
        },
        {
          value: '9',
          label: 'zip'
        },
        {
          value: '10',
          label: 'rar'
        }
      ],
      fileExtend: '',
      password: ''
    }
  },
  computed: {
    cloudExtract() {
      const flag = this.fileName && this.fileExtend
      if(this.fileType === 'public') {
        return flag
      }
      return flag && this.password
    }
  }
}
</script>

<style lang="less">
.other {
  padding: 0 10px 0px 20px;
  color: #606266;
  font-size: 14px;
  input {
    width: 32px;
    margin-left: 5px;
    outline: none;
    border: 1px solid #eeeeee;
    padding: 5px;
    border-radius: 2px;
  }
}
.download {
  width: 32%;
  margin: 0 auto;
  color: #333333;
  .slogan {
    padding-top: 30px;
  }
  .common-box {
    position: relative;
    margin-top: 20px;
    .download-slogan {
      font-size: 20px;
    }
    .extract-box {
      padding: 10px 0 80px 0;
      .download-tip {
        font-size: 14px;
        margin: 20px 0;
      }
      .extract-method {
        display: flex;
        align-items: center;
        justify-content: center;
        .common-input {
          margin-left: 5px;
        }
        .dot {
          font-size: 30px;
          text-align: center;
        }
      }
      .el-radio-group {
        margin: 15px 0;
      }
      .extract-button {
        width: 25%;
        margin: 0 auto;
        padding: 10px 15px;
        background-color: #e0e0e0;
        color: #ffffff;
        font-size: 18px;
        border-radius: 8px;
        margin-top: 10px;
        &.active {
          background-color: #35AC70;
        }
      }
    }
    .use-file-name {
      position: absolute;
      right: 0px;
      bottom: 0px;
      padding: 10px;
      border-radius: 0;
      border-top-left-radius: 30px;
    }
  }
}
</style>
