<template>
  <div class="main">
    <div :class="{three:index<3}" class="index">{{index+1}}</div>
    <div class="content">
      <div class="title">
        <img class="cover" v-if="news.cover" :src="news.cover" referrerPolicy="no-referrer">
        <span class="title-content">{{news.title}}</span>
      </div>
      <div class="desc">
        {{news.custom_description || news.description}}
      </div>
      <div class="from">
      <span class="author">
        {{(news.user[0] && news.user[0].name)||
        (news.group[0] && news.group[0].name)
        }}
      </span>
        <span class="text">发布于</span>
        <span class="book">
        {{news.book[0] && news.book[0].name}}
      </span>
      </div>
    </div>
  </div>
</template>

<script>
  import {emitMixin} from '../../mixin'
  export default {
    name: "News",
    props: {
      news: {
        type: Object,
        default() {
          return {}
        }
      },
      index: {
        type: Number,
        default: 0
      }
    },
    mixins:[emitMixin],
  }
</script>

<style scoped>
  .main {
    background-color: #fff;
    border-bottom: 1px solid rgba(0, 0, 0, .1);
    padding: 16px 20px;
  }
  .content{
    margin-left: 30px;
  }
  .title {
    margin-bottom: 12px;
  }

  .index {
    width: 20px;
    float: left;
    font-weight: 700;
    font-size: 20px;
    line-height: 1;
  }

  .title-content {
    font-weight: 500;
    font-size: 16px;
    line-height: 1.3;
    color: #262626;
  }
  .cover{
    width: 96px;
    height: 60px;
    float: right;
    border-radius: 2px;
    margin-left: 16px;
  }
  .three {
    color: #FA541C;
  }

  .desc {
    color: #93918E;
    margin-top: 12px;
    margin-bottom: 18px;
    line-height: 1.5;
  }

  .from {
    color: #93918E;
    font-size: 12px;
    margin-bottom: 8px;
  }

  .from .author, .from .book {
    color: #5E6676;
  }

</style>
