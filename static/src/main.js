import Vue from 'vue'
import App from './App.vue'
import voteClass from './components/vote-class.vue'
import helloScreen from './components/hello-screen.vue'

Vue.component('vote-class', voteClass);
Vue.component('hello-screen', helloScreen);

new Vue({
  el: '#app',
  render: h => h(App),
  components: {
  	'vote-class': voteClass,
  	'hello-screen': helloScreen,
  }
})