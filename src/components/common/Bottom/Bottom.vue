<template>
  <div class="footer">
    <div class="title">
      <img src="~@/assets/img/logo.svg" alt="">
      <span class="text">十万阿里人都在用的笔记与文档知识库</span>
    </div>
    <div class="link">
      <a href="" class="about">关于语雀</a>
      <a href="" class="desktop">桌面版本</a>
      <div class="sep"></div>
      <a href="" class="english">English</a>
      <a href="" class="register">快速注册</a>
    </div>
    <div class="copy">
      <p class="info">&copy; 经营许可证编号： 合字B2-20190051</p>
      <a class="id" href="http://www.beian.miit.gov.cn/">ICP备案号: 浙ICP备16025414号-3</a>
    </div>
  </div>
</template>

<script>
  import {emitMixin} from '../../../mixin'

  export default {
    name: "Bottom",
    mixins:[emitMixin],
  }
</script>

<style scoped>
  .footer {
    width: 100%;
    background-color: #F5F6F7;
  }

  .title {
    padding: 30px 0 10px;
    text-align: center;
  }

  .title img {
    width: 64px;
    height: 22px;
    min-width: 64px;
    vertical-align: middle;
    margin-right: 12px;
    margin-bottom: 1px;
  }

  .title p {
    font-size: 14px;
    line-height: 22px;
  }

  .link {
    background-color: #F5F6F7;
    line-height: 14px;
    height: 14px;
    width: 100%;
    border: none;
    display: flex;
    padding: 0 40px;
  }

  .link .sep {
    border-left: 1px solid rgba(0, 0, 0, .1);
  }

  .copy {
    color: #ACACAD;
  }

  .link {
    margin-bottom: 15px;
  }


  .link a {
    color: #ACACAD;
    flex: 1;
    font-size: 14px;
    text-decoration: none;
  }

  a:visited {
    text-decoration: none;
  }

  .english {
    color: #31CC79;
  }

  .copy {
    font-size: 12px;
    text-align: center;
    height: 45px;
  }
  .copy .id{
    color: #ACACAD;
    text-decoration:none;
  }

  .copy .id:visited{
    color: #ACACAD;
    text-decoration:none;
  }

</style>
