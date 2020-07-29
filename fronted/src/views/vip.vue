<template>
  <div class="vip-wrapper">
    <div v-if="isVip" class="vip-tips">
      You are already a vip
    </div>
    <div v-else class="be-vip">
      <div>
        <label for="charge">charge:</label>
        <input 
          id="charge" class="common-input" 
          v-model.number="chargeNum"
          placeholder="large than $10 will be vip"
        />
      </div>
      <button class="extract" @click="getVip">be vip</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '../api/index'
export default {
  name: 'Vip',
  data() {
    return {
      chargeNum: 0
    }
  },
  computed: {
    ...mapState(['isVip'])
  },
  methods: {
    getVip() {
      if(this.chargeNum > 0) {
        if(localStorage.getItem('Authorization')) {
          this.axios({
            method: 'post',
            url: api.vip,
            data: {
              charge: this.chargeNum,
            },
            transformRequest: [
              function (data) {
                let ret = ''
                for (let it in data) {
                  ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
                }
                ret = ret.substring(0, ret.lastIndexOf('&'));
                return ret
              }
            ],
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
          }).then(() => {
            this.$store.dispatch('beVip')
          })
        }
      }
    }
  }
}
</script>

<style lang="less">
.vip-wrapper {
  color: #42BD86;
  .vip-tips {
    padding-top: 100px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
  }
  .be-vip {
    padding-top: 200px;
    text-align: center;
    .common-input {
      margin-left: 10px;
    }
  }
  .extract {
    outline: none;
    border: none;
    margin-top: 10px;
  }
}
</style>
