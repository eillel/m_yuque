<template>
  <div class="main">
    <div v-if="index === 0">
      <router-link :to="url" tag="div">
        <div>
          <img class="cover" :src="session.cover" referrerPolicy="no-referrer">
          <div class="title">{{session.title}}</div>
        </div>
      </router-link>
      <div class="from">
        <span class="author">
          {{(session.user[0] && session.user[0].name)||
          session.group[0] && session.group[0].name
          }}
        </span>
        <span>发布于</span>
        <span class="book">
          {{session.book[0].name}}
        </span>
        <span class="date">{{session.created_at.split('T')[0]}}</span>
      </div>
    </div>
    <div v-if="index > 0">
      <router-link :to="url" tag="div">
        <div>
          <img class="cover-small" :src="session.cover" referrerPolicy="no-referrer">
          <div class="title">{{session.title}}</div>
          <p class="desc">{{session.custom_description||session.description}}</p>
        </div>
      </router-link>
      <div class="from">
        <span class="author">
          {{(session.user[0] && session.user[0].name)||
          session.group[0] && session.group[0].name
          }}
        </span>
        <span>发布于</span>
        <span class="book">
          {{session.book[0].name}}
        </span>
        <span class="date">{{session.created_at.split('T')[0]}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  import {emitMixin} from '../../mixin'

  export default {
    name: "Session",
    mixins: [emitMixin],
    props: {
      index: {
        type: Number,
        default: 0
      },
      session: {
        type: Object,
        default() {
          return {}
        }
      }
    },
    computed:{
      url(){
        return {
          // name:'Detail',
          // params:{
          //   doc_id:this.session.id
          // }
        }
      }
    }

  }
</script>

<style scoped>
  .main {
    padding: 16px;
    border-bottom: 1px solid rgba(0, 0, 0, .1);
  }

  .cover {
    width: 100%;
  }

  .title {
    margin-bottom: 12px;

    font-weight: 700;
    font-size: 16px;
    line-height: 1.3;
    color: #262626;
  }

  .title:visited {
    color: #515a6e;
  }

  .cover-small {
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
    max-height: 50px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;

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
