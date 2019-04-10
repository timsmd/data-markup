<template>
	<div id='app'>
		<div id='nav-bar' class='bg-dark text-light'>
			<nav-bar :login_info="this.login_info" @redirect_route="redirect" @loggedInState="login_update"></nav-bar>
		</div>
		<div id='main-body' class='bg-white text-dark'>
			<hello-screen v-if='display_module === 1' @redirect_route="redirect" id='hello-screen'></hello-screen>
			<vote-class :login_info="this.login_info" v-if='display_module === 2' id='vote-class'></vote-class>
			<sign-in v-if="display_module === 3"  @redirect_route="redirect" @loggedInState="login_update" id="sign-in"></sign-in>
		</div>
	</div>
</template>

<script>
 	import axios from 'axios';
 	export default {
		name: 'app',
		data: function () {
			return {
				display_module: 0,
				login_info: {
					logged_in: null,
					current_user: '',
				},
			}
		},
		created: function() {
			this.check_login();
			// TODO fix this
			this.display_module = this.login_info.logged_in ? 2 : 1;
		},
		methods: {
			check_login: function () {
				axios.get('/api/check_login')
				.then(response => {
					this.login_info.logged_in = response.data.logged_in;
					this.login_info.current_user = response.data.username || '';
				})
			},
			login_update: function (info) {
				this.login_info.logged_in = info.logged_in;
				this.login_info.current_user = info.current_user;
			},
			redirect: function (route) {
				this.display_module = route;
			},
		}
	}
</script>

