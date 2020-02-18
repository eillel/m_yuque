<template>
  <div class="main">
    <div class="content">
      <router-link :to="url" tag="div">
        <div class="title">
          <img class="cover" v-if="news.cover" :src="news.cover" referrerPolicy="no-referrer">
          <span class="title-content">{{news.title}}</span>
        </div>
      </router-link>
      <div class="desc">
        {{news.custom_description || news.description}}
      </div>
      <div class="from">
        <div class="like">
          <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
          <span class="number">{{news.likes_count}}</span>
        </div>
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
    mixins: [emitMixin],
    computed: {
      url() {
        return {
          // name: 'Detail',
          // params: {
          //   book_id: this.news.book_id,
          //   slug: this.news.slug
          // }
        }
      }
    }
  }
</script>

<style scoped>
  .main {
    background-color: #fff;
    border-bottom: 1px solid rgba(0, 0, 0, .1);
    padding: 16px;
  }

  .content {

  }

  .like {
    width: 50px;
    display: inline-block;
    text-align: center;
    height: 24px;
    background-color: #FAFAFA;
    vertical-align: center;
    margin-right: 5px;
  }

  .number {
    margin-left: 10px;
    width: 56px;
    color: #000;
    font-size: 12px;
    line-height: 24px;
    height: 24px;
  }

  .fa {
    color: #FAB121;
  }

  .title {
    margin-bottom: 12px;
  }

  .title-content {
    font-weight: 700;
    font-size: 16px;
    line-height: 1.3;
    color: #262626;
  }

  .cover {
    width: 96px;
    height: 60px;
    float: right;
    border-radius: 2px;
    margin-left: 16px;
  }

  .desc {
    color: #93918E;
    margin-top: 12px;
    margin-bottom: 18px;
    line-height: 1.5;
    max-height: 80px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: pre-wrap;
  }

  .from {
    color: #93918E;
    font-size: 12px;
  }

  .from .author, .from .book {
    color: #5E6676;
  }

</style>
