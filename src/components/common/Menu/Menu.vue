<template>
  <div class="content">
    <div class="search">
     <div class="search-mid">
        <Icon class="search-icon" type="ios-search"/>
       <input v-model="keyword" class="search-input" placeholder="搜索"/>
       <Icon class="search-icon-close" @click="keyword=''" v-show="keyword" type="md-close-circle" />
     </div>
      <div v-show="keyword"  class="search-hint">
        <div v-text="keyword" class="search-content">
        </div>
        <div class="search-yc">
          搜索语雀
        </div>
      </div>
    </div>
    <div class="others">
      <div>产品功能</div>
      <div>数据安全</div>
      <div>空间</div>
      <div>发现</div>
    </div>
  </div>
</template>

<script>


  export default {
    name: "Menu",
    data(){
      return {
        keyword: ''
      }
    },
    components: {}

  }
</script>

<style scoped>
  .content {
    width: 100%;
    position: fixed;
    background-color: #fff;
  }
  .search-icon-close {
   padding-right: 6px;
    color: #D9D9D9;
  }
  .search {
    width: 100%;
    padding: 16px 16px 4px 16px;
    display: block;
   text-align: center;
  }

  .search-mid {
    background-color: #F5F5F5;
  }

  .search-input {
    border: none;
    background-color: #F5F5F5;
    height: 32px;
    width: 90%;
    padding-left: 5px;
    color: #595959;
  }

  .search-input::placeholder {
    color: #CDCDCD;
    font-size: 14px;
  }

  .search-input:focus {
    outline: none;
  }
  .search-yc{
    color: #B4BBB6;
    line-height: 16px;
    font-size: 16px;
    position: absolute;
    top: 0; right: 0; bottom: 0;
    width: 80px;
    height: 18px;
    margin: auto;
  }
  .search-hint {
    margin-top: 3px;
    width: 90%;
    height: 48px;
    border-radius: 3px;
    position: fixed;
    background-color: #E9F7EC;
    border-top: 3px solid #fff;
    border-bottom: 3px solid #fff;
    box-shadow: 1px 2px 5px rgba(100,100,100,.2);
  }
  .search-content{
    color: #B4BBB6;
    line-height: 16px;
    font-size: 16px;
    position: absolute;
    left: 0; top: 0; bottom: 0;
    height: 16px;
    width: 77%;
    text-align: left;
    padding-left: 5px;
    overflow: hidden;
    margin: auto;

  }

  .others{
    color: #8C8C8C;
    font-size: 18px;
    margin-left: 5%;
    padding-top: 5px;
  }
  .others div{
    margin-top: 10px;
  }
</style>
