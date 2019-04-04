<template>
	<div id="app">
		<h1>App says: {{ msg }}</h1>
		<p>login form</p>
		<input v-model="username" placeholder="username">
		<input v-model="password" placeholder="password">
		<button v-on:click="login">Login</button>
		<button v-on:click="logout">Logout</button>
		<p>sign up form</p>
		<button v-on:click="signup">Sign up</button>
		<p>voting classes</p>
		<div v-for="item in this.profile_classes">
			<input type="radio" v-bind:id="item.id" value="Один" v-bind:name="item.id+'_'">
			<label for="one">{{ item.if_true }}</label>
			<input type="radio" v-bind:id="item.id" value="Два" v-bind:name="item.id+'_'">
			<label for="two">{{ item.if_false }}</label>
			<br>
		</div>
	</div>
</template>

<script>
 	import axios from 'axios';
 	export default {
		name: 'app',
		data() {
			return {
				msg: '',
				username: '',
				password: '',
				profiles: [],
				profile_classes: [],
				errors: []
			}
		},
		created: function () {
				axios.get('/api/classes')
				.then(response => {
					this.profile_classes = response.data.classes
				})
				.catch(e => {
					this.errors.push(e)
				})
			},
		// get classes from db on created page
		methods: {
			login: function () {
				if (this.username != '' && this.password != '') {
					axios.post('/api/login', {
						username: this.username,
						password: this.password
					})
					.then(response => {
						if (response.data.logged_in) {
							this.msg = response.data.username + ' logged in'
						}
					})
					.catch(e => {
						this.errors.push(e)
					})
				}
			},
			signup: function () {
				if (this.username != '' && this.password != '') {
					axios.post('/api/signup', {
						username: this.username,
						password: this.password
					})
					.then(response => {
						this.msg = response.data.username + ' signed up'
					})
					.catch(error => {
						this.errors.push(error)
					})
				}
			},
			logout: function () {
				axios.get('/api/logout')
				.then(response => {
					this.msg = response.data.logged_out
				})
				.catch(e => {
					this.errors.push(e)
				})
			},
			vote: function () {

			},
			get_profile: function () {

			}
		}
	}
</script>

