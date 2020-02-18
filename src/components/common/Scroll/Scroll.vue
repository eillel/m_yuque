<template>
  <div>
    <div v-show="show" class="back2top" @click="back2top"><img src="~@/assets/img/back2top.svg"></div>
    <div ref="wrapper" class="wrapper">
      <div class="content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
  import BScroll from 'better-scroll'

  export default {
    name: "Scroll",
    data() {
      return {
        scroll: null,
      }
    },
    computed: {
      show() {
        return this.getY() < -700
      }
    },
    methods: {
      back2top() {
        this.scrollTo(0, 200)
      },
      refresh() {
        this.scroll && this.scroll.refresh()
      },
      getY() {
        return this.scroll ? this.scroll.y : 0
      },
      scrollTo(y, delay = 0) {
        this.scroll && this.scroll.scrollTo(this.scroll.x, y, delay)
        this.refresh()
      },
      isScrollDown() {
        return this.scroll.directionY === -1
      },
      isScrollUp() {
        return this.scroll.directionY === 1
      },
      pullLoadMore() {
        this.$emit('pullLoadMore')
        this.scroll.finishPullUp()
        this.refresh()
      }
    },
    mounted() {
      this.scroll = new BScroll(this.$refs.wrapper, {
        probeType : this.probeType,
        pullUpLoad: this.pullUpload,
        click:true,
        swipeTime:1000,

      })
      if (this.probeType === 2 || this.probeType === 3) {
        this.scroll.on('scroll', () => {
          this.$emit('scroll', this.scroll.y)
        })
      }
      if (this.pullUpload) {
        this.scroll.on('pullingUp', () => {
          this.pullLoadMore()
        })
      }

    },
    props: {
      probeType: {
        type: Number,
        default: 0
      },
      pullUpload: {
        type: Boolean,
        default: false
      },
    },
    deactivated(){
      this.scroll.stop()
    }
  }
</script>

<style scoped>
  .wrapper {
    height: calc(100vh - 100px);
    position: relative;
    z-index: 1;
  }

  .back2top img {
    position: fixed;
    bottom: 20px;
    right: 16px;
    width: 35px;
    height: 35px;
    margin: auto;
    color: #31CA79;
    border-radius: 100%;
    background-color: #fff;
    z-index: 2;
  }
</style>
