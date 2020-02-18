<template>
  <div>
    <div class="scroll">
      <scroll ref="scroll"

              :probeType="3"
              @scroll="scroll">
        <book :key="item.id" v-for="(item,index) in data" :book="item" :index="index" />
        <bottom/>
      </scroll>
    </div>
  </div>
</template>

<script>
  import api from '../../network/'
  import Book from './Book'
  import Bottom from '../../components/common/Bottom/Bottom'
  import Scroll from '../../components/common/Scroll/Scroll'
  import {loadedMixin,activeMixin} from '../../mixin'

  export default {
    name: "Repos",
    data() {
      return {
        page: 1,
        data: [],
      }
    },
    methods: {
    },
    created() {
      api.getBooks().then(data => {
        this.data = data.data.data
      })
    },
    components: {
      Book,
      Bottom,
      Scroll,
    },
    mixins:[loadedMixin,activeMixin]
  }
</script>

<style scoped>

</style>
