<template>
	<div>
		<nav class="navbar navbar-light">
				<a class="navbar-brand" v-if="logged_in">Hello, {{ username }}!</a>
				<button type="button" class="btn btn-light" v-if="logged_in">Logout</button>
				<button type="button" class="btn btn-light" v-else="logged_in">Login</button>

		</nav>
	</div>
</template>

<script>
	import axios from 'axios'
	export default {
		name: 'nav-bar',
		props: [],
		data: function () {
			return {
				logged_in: false,
				username: '',
			}
		},
		created: function () {
			this.login = this.check_login();
		},
		methods: {
			check_login: function () {
				axios.get('/api/check/login')
				.then(response => {
					this.logged_in = response.data.logged_in;
					this.current_user = response.data.username || '';
			})
			}
		}
	}
</script>