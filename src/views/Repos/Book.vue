<template>
  <div class="main">
    <div class="title">
      <span :class="{three:index<3}" class="title-index">{{index+1}}</span>
      <span class="title-content">{{book.name}}</span>
    </div>
    <div class="desc">
      {{book.description}}
    </div>
    <div class="from">
      <span class="text">来自</span>
      <span class="author">
        {{(book.user[0] && book.user[0].name)||
        (book.group[0] && book.group[0].name)
        }}
      </span>
    </div>
  </div>

</template>

<script>
  import {emitMixin} from '../../mixin'
  export default {
    name: "Book",
    props: {
      book: {
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
    mixins:[emitMixin]

  }
</script>

<style scoped>
  .main {
    background-color: #fff;
    width: 100%;
    border-bottom: 1px solid rgba(0, 0, 0, .1);
    padding: 12px 20px;
  }

  .title {
    margin-bottom: 12px;
  }

  .title-index {
    font-weight: 700;
    font-size: 20px;
    line-height: 1;
  }

  .title-content {
    font-size: 16px;
    line-height: 1.3;
    color: #262626;
    margin-left: 10px;
  }

  .three {
    color: #FA541C;
  }

  .desc {
    color: #93918E;
    margin-left: 10px;
    padding-left: 14px;
    margin-bottom: 12px;

  }

  .from {
    color: #93918E;
    font-size: 12px;
    margin-left: 10px;
    padding-left: 14px;
  }

  .from .author {
      color: #5E6676;
  }
</style>
