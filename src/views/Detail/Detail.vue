<template>
  <div class="content">
    <div v-html="doc&&doc.content"></div>
  </div>
</template>

<script>
  import api from '@/network'

  export default {
    name: "Detail",
    props: {},
    data() {
      return {
        doc:null
      }
    },
    mounted() {
      api.getDocs({id: this.$route.params.doc_id}).then(data => {
        this.doc =data.data.data[0]
        // this.doc.content = decodeURIComponent(this.doc.content)
      })
    },
  }
</script>

<style scoped>

</style>
