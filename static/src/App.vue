<template>
	<div id="app">
		<h1>App says: {{ msg }}</h1>
		<input v-model="postInput" placeholder="input text">
		<button v-on:click="postButton">Press</button>
		<p>login form</p>
<!-- 		<input v-model="username" placeholder="username">
		<input v-model="password" placeholder="password"> -->
		<button v-on:click="login">Login</button>
		<p>sign up form</p>
		<input v-model="username" placeholder="username">
		<input v-model="password" placeholder="password">
		<button v-on:click="signup">Sign up</button>
	</div>
</template>

<script>
 	import axios from 'axios';

 	export default {
		name: 'app',
		data() {
			return {
				msg: '',
				postInput: '',
				username: '',
				password: '',
				errors: []
			}
		},
		created() {
			axios.get("/api/properties").then(r =>{
				this.msg = r.data
			})
		},
		methods: {
			postButton : function () {
				axios.post('/api', {
					data: this.postInput
				})
				.then(response => {
					this.msg = response.data.data
				})
				.catch(e => {
					this.errors.push(e)
				})
			},
			login: function () {
				axios.post('/api/login', {
					username: this.username,
					password: this.password
				})
				.then(response => {
					this.msg = response.data.username + ' logged in'
				})
				.catch(e => {
					this.errors.push(e)
				})
			},
			signup: function () {
				axios.post('/api/signup', {
					username: this.username,
					password: this.password
				})
				.then(response => {
					this.msg = response.data.username + ' signed up'
				})
				.catch(e => {
					this.errors.push(e)
				})
			}
		}
	}
</script>

