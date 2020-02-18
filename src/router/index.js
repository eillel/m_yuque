import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const Headlines = ()=> import('../views/Headlines/Headlines')
const Docs = ()=> import('../views/Docs/Docs')
const Repos = ()=> import('../views/Repos/Repos')
const Detail = ()=> import('../views/Detail/Detail')
const routes = [
  {
    path: '/headlines',
    name: 'Headlines',
    meta:{
      title:'推荐'
    },
    component: Headlines
  },
  {
    path: '/docs',
    name: 'Docs',
    meta:{
      title:'热门文章'
    },
    component: Docs
  },
  {
    path: '/repos',
    name: 'Repos',
    meta:{
      title:'热门知识库'
    },
    component:Repos
  },
  {
    path:'/detail',
    name: 'Detail',
    component:Detail
  },
  {
    path: '',
    redirect:'/headlines'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to,from,next)=>{
  document.title = to.matched[0].meta.title ||'首页'
  next()
})
export default router
