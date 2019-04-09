<template>
	<div id='app'>
		<div id='nav-bar' class='bg-dark text-light'>
			<nav-bar></nav-bar>
		</div>
		<div id='main-body' class='bg-light text-dark'>
			<button @click='change'>change</button>
			<vote-class v-if='modifiers.show_vote' id='vote-class'></vote-class>		
			<hello-screen v-if='modifiers.show_hello' id='hello-screen'></hello-screen>
		</div>
	</div>
</template>

<script>
 	import axios from 'axios';
 	export default {
		name: 'app',
		data: function () {
			return {
				msg: '',
				modifiers: {
					show_vote: false,
					show_hello: true,
				},
				current_user: '',
				logged_in: '',
				username: '',
				password: '',
				profiles: [],
				profile_classes: [],
				errors: [],
				current_profile: 4,
			}
		},
		created: function () {
			axios.get('/api/check/login')
			.then(response => {
				this.logged_in = response.data.logged_in;
				this.current_user = response.data.username || '';
			})
		},
		methods: {
			change: function () {
				this.modifiers.show_vote = !this.modifiers.show_vote;
				this.modifiers.show_hello = !this.modifiers.show_hello;
			},
			login: function () {
				if (this.username != '' && this.password != '') {
					axios.post('/api/login', {
						username: this.username,
						password: this.password
					})
					.then(response => {
						if (response.data.logged_in) {
							this.logged_in = true;
							this.current_user = response.data.username;
							this.msg = this.current_user + ' logged in';
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
					// TODO handle data(logged in flag & current user) on logout
					this.msg = response.data.logged_out
				})
				.catch(e => {
					this.errors.push(e)
				})
			},
		}
	}
</script>

