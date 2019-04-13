import Vue from 'vue'
import VueCookies from 'vue-cookies'
import App from './App.vue'
import voteClass from './components/vote-class.vue'
import helloScreen from './components/hello-screen.vue'
import navBar from './components/nav-bar.vue'
import signIn from './components/sign-in.vue'

Vue.use(VueCookies);
Vue.component('vote-class', voteClass);
Vue.component('hello-screen', helloScreen);
Vue.component('nav-bar', navBar);
Vue.component('sign-in', signIn);

new Vue({
    el: '#app',
    render: h => h(App),
    components: {
        'vote-class': voteClass,
        'hello-screen': helloScreen,
        'nav-bar': navBar,
        'sign-in': signIn,
    }
})