<template>
  <div>
    <div class="top">
      <div class="menu" @click="menu">
        <Icon v-show="!menuShow" type="ios-menu"/>
        <Icon v-show="menuShow" type="md-close"/>
      </div>
      <div class="title">
        <slot name="title">
          <img src="~@/assets/img/logo.svg" alt="">
        </slot>
      </div>
      <div class="icon">
        <i class="bell fa fa-bell fa-lg"></i>
        <Icon class="add" type="ios-add-circle"/>
      </div>
    </div>

    <Menu v-if="menuShow"/>
    <div v-if="menuShow" class="mask"></div>

  </div>
</template>

<script>
  import Menu from '../Menu/Menu'

  export default {
    name: "NavBar",
    data() {
      return {
        theme1: 'light',
        menuShow: false
      }
    },
    methods: {
      menu() {
        this.menuShow = !this.menuShow
      }
    },
    components: {
      Menu
    }
  }
</script>

<style scoped>

  .top {
    display: flex;
    width: 100%;
    height: 50px;
    align-items: center;
    justify-content: space-between;
    position: relative;
  }

  .menu {
    width: 120px;
    font-size: 28px;
    margin-left: 8px;
    flex: 1;
  }

  .title {
    width: 130px;
  }

  .title img {
    width: 82px;
    height: 28px;
  }

  .icon {
    flex: 1;
    width: 120px;
    justify-content: flex-end;
    align-items: center;
    display: flex;
  }

  .bell {
    font-size: 17px;
    position: relative;
  }

  .add {
    position: relative;
    width: 50px;
    line-height:50px;
    font-size: 25px;
    color: #26B863;
  }

</style>
