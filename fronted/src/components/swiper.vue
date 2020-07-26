<template>
  <div class="myswiper-wrapper">
    <swiper ref="mySwiper" :options="swiperOption">
      <swiper-slide 
        v-for="item in swiperImg"
        :key="item.id"
        style="width:652px;"
      >
        <div
          class="mySlideItem" 
          :style="{
            backgroundImage:`url(${item.img})`
          }">
          <div class="silder-text" v-html="item.text" />
        </div>
      </swiper-slide>
      <div class="swiper-button-prev" slot="button-prev" />
      <div class="swiper-button-next" slot="button-next" />
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'
export default {
  name: '',
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      swiperOption: {
        loop: true,
        autoplay: true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      },
      swiperImg: [
        {
          id: 1,
          text: '<p>After uploading, the file <span>can be downloaded</span> <br>with <span>6-digit extraction code</span></p>',
          img: require('../assets/images/privateicon-76c04dbabe.png'),
        },
        {
          id: 2,
          text: 'After uploading, <span>scan the code</span> and save the<span> 6-bit extracted</span><br> code to prevent forgetting to extract information',
          img: require('../assets/images/stringicon-03f932590f.png'),
        },
        {
          id: 3,
          text: 'After the approval of the files that are willing to <span>share</span>, <br>the files will <span>be published and shared</span> <br>in the <span>document community</span>',
          img: require('../assets/images/shareicon-c21984eb1a.png'),
        }
      ]
    }
  }
}
</script>

<style lang="less">
.myswiper-wrapper {
  width: 55%;
  .mySlideItem {
    height: 400px;
    background-size: contain;
    background-repeat: no-repeat;
    font-weight: 700;
    font-size: 18px;
    .silder-text {
      color: #333333;
      text-align: center;
      padding-top: 170px;
      line-height: 32px;
      span {
        color: #66CC99;
      }
    }
  }
  .swiper-button-prev, .swiper-button-next{
    color: #66CC99;
  }
}
</style>
