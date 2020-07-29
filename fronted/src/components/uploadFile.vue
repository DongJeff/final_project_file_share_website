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
                :action="action"
                :headers="headers"
                :file-list="fileList"
                auto-upload
                :before-upload="beforeUpLoadHandler"
                :on-success="successHandler"
                :on-error="errorHandler"
                :disabled="isBanSubmit"
        >
            <i class="el-icon-upload"/>
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
                :share-code="code"
        />
    </div>
</template>

<script>
    import ExtractCode from '../components/extractCode'
    import SuccessTip from '../components/successTip'
    import api from '../api/index'
    import axios from "axios";

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
                iShowSuccessTips: false,
                filename: '',
                action: axios.defaults.baseURL + api.upload,
                headers: {
                    'token': localStorage.getItem('Authorization'),
                },
                code: ''
            }
        },
        methods: {
            beforeUpLoadHandler(file) {
                if (!this.$store.state.isVip && file.size / 1024 / 1024 > 10) {
                    this.$message({
                        message: 'You are not vip, upload file should less then 10MB',
                        type: 'warning'
                    })
                    return false
                }
                this.headers['Content-Disposition'] = `attachment; filename=${file.name}`
            },
            successHandler(response) {
                this.fileList = []
                console.log("--->"+JSON.stringify(response))
                if (response.code===401){
                    this.$store.dispatch('logout')
                    this.$router.push({path: "/"})
                    this.$message({
                        message: "token is not valid",
                        type: 'warning'
                    })
                }
                this.code = response.share_code
                this.iShowSuccessTips = true
            },
            errorHandler(response) {
                this.fileList = []
                console.log("--->"+JSON.stringify(response))
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
