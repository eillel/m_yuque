<template>
  <div>
    <div class="scroll">
      <scroll ref="scroll"

              :probeType="3"
              @scroll="scroll">
        <news :key="item.id" v-for="(item,index) in data" :news="item" :index="index"></news>
        <bottom></bottom>
      </scroll>
    </div>
  </div>
</template>

<script>
  import api from '../../network/'
  import News from './News'
  import Bottom from '../../components/common/Bottom/Bottom'
  import Scroll from '../../components/common/Scroll/Scroll'
  import {loadedMixin,activeMixin} from '../../mixin'

  export default {
    name: "Docs",
    data() {
      return {
        page: 1,
        data: [],
      }
    },
    methods: {
    },
    created() {
      api.getDocs().then(data => {
        this.data = data.data.data
      })
    },
    components: {
      Bottom,
      News,
      Scroll,
    },
    mixins: [loadedMixin,activeMixin]
  }
</script>

<style scoped>

</style>

