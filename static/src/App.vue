<template>
	<div id='app'>
		<div id='nav-bar'>
			<!-- -->
		</div>
		<div id='main-body'>
			<vote-class id='vote-class'></vote-class>		
			<!-- -->
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
				current_user: '',
				logged_in: '',
				username: '',
				password: '',
				profiles: [],
				profile_classes: [],
				errors: [],
				current_profile: 4,
				votes: [
					{
						class: 1,
						value: 0
					},
					{
						class: 2,
						value: 0
					}
				]
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

