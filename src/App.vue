<template>
  <div id="app">
    <div class="nav">
        <head-bar></head-bar>
    </div>
    <div class="link">
      <router-link tag="span" active-class="active" class="link-span" to="/headlines">推荐</router-link>
      <router-link tag="span" active-class="active" class="link-span" to="/docs">热门文章</router-link>
      <router-link tag="span" active-class="active" class="link-span" to="/repos">热门知识库</router-link>
    </div>
    <div class="content">
      <keep-alive exclude="Detail"><router-view/></keep-alive>
    </div>
  </div>
</template>
<script>
  import HeadBar from './components/common/HeadBar/HeadBar'
  import Scroll from './components/common/Scroll/Scroll'
  import {debounce} from './util'

  export default {
    name: "App",
    data() {
      return {
        refresh: null
      }
    },
    methods: {
      scroll() {
        console.log('scroll')
      }
    },
    components: {
      HeadBar,
      Scroll,
    },

  }
</script>
<style>
  .nav,.link {
    position: relative;
    z-index: 2;
    background-color: #fff;
  }
.content{
  position: relative;
  z-index: 1;
}

  .link {
    background-color: #fff;
    width: 100%;
    text-align: center;
    display: flex;
    height: 50px;
    border-top: 1px solid rgba(0, 0, 0, .1);
    border-bottom: 1px solid rgba(0, 0, 0, .1);
  }

  .link-span {
    font-size: 18px;
    height: 18px;
    line-height: 18px;
    margin: auto;
  }

  .active {
    font-weight: 700;
  }
</style>
