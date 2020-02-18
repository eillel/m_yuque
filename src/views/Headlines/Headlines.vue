<template>
  <div>
    <div class="scroll">
      <scroll ref="scroll"
              :pullUpload="true"
              @pullLoadMore="getMore"

              :probeType="3"
              @scroll="scroll">
        <div class="recommend">
          <p>小编精选</p>
          <a>往期</a>
        </div>
        <session v-for="(session,index) in selections" :key="session.id" :index="index" :session="session"/>
        <news v-for="(news , index) in data" :key="news.id" :index="index" :news="news"/>
      </scroll>
    </div>
  </div>
</template>

<script>
  import api from '../../network/'
  import Session from './Session'
  import News from './News'
  import Scroll from '../../components/common/Scroll/Scroll'
  import {loadedMixin, activeMixin} from '../../mixin'

  export default {
    name: "Headlines",
    data() {
      return {
        page: 2,
        data: [],
        selections: [],
      }
    },
    components: {
      Session,
      News,
      Scroll,
    },
    methods: {
      getMore() {
        api.getDocs({page: ++this.page}).then(data => {
          this.data.push(...data.data.data)
        })
      }
    },
    created() {
      api.getDocs({page: this.page++}).then(data => {
        this.selections = data.data.data.filter(item => Number(item.cover) !== 0).slice(0, 4)
      })
      api.getDocs({page: this.page}).then(data => {
        this.data = data.data.data
      })
    },
    mixins: [loadedMixin, activeMixin]
  }
</script>

<style scoped>
  .recommend {
    width: 100%;
    position: relative;
    vertical-align: center;
    height: 48px;
    border-bottom: 1px solid rgba(0, 0, 0, .1);
    display: flex;
    padding: 12px 16px;
    justify-content: space-between;
    align-items: center;
  }

  .recommend:first-child {
    font-weight: 400;
    margin-bottom: 0;
    line-height: 1.5;
    font-size: 16px;
    color: #262626;
  }

  .recommend a {
    text-decoration: none;
    outline: none;
    cursor: pointer;
    color: #8c8c8c;
  }
</style>
