import axios from 'axios'
import Vue from 'vue'


// Vue.prototype.$http = axios
const protocol = 'http'
const host = '127.0.0.1'
const port = 9000
const timeout = 5000
const baseURL = `${protocol}://${host}:${port}/api`

axios.defaults.baseURL = `${protocol}://${host}:${port}/api`
const instance = axios.create({
  headers:{
    'Content-Type':'application/json'
  },
  withCredentials:true   //加了这段就可以跨域了
})




export default {
  getBooks(params) {
    return instance.get('books', {
      query: params||{}
    })
  },
  getDocs(params) {
    return instance.get('docs', {
      params: params||{}
    })
  },
  getUsers(params) {
    return instance.get('users', {
      query: params||{}
    })
  }
}
