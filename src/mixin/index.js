import {debounce} from '../util'

export const emitMixin = {
  mounted() {
    this.$bus.$emit('loaded')
  }
}
export const loadedMixin = {
  mounted() {
    this.refresh = debounce(this.$refs.scroll.refresh, 50)
    this.$bus.$on('loaded', () => {
      this.refresh()
    })
  }
}

export const activeMixin = {
  data() {
    return {
      y: 0,
      setY: null
    }
  },
  mounted() {
    this.setY = debounce((y) => {
      this.y = y
    }, 200)
  },
  deactivated() {
    this.y = this.$refs.scroll.getY()
  },
  activated() {
    this.$refs.scroll.scrollTo(this.y)
  },
  methods: {
    scroll(y) {
      this.setY(y)
    }
  }
}
