<template>
	<div id='app'>
		<div id='nav-bar' class='bg-dark text-light'>
			<nav-bar></nav-bar>
		</div>
		<div id='main-body' class='bg-light text-dark'>
			<vote-class v-if='modifiers.show_vote' id='vote-class'></vote-class>
			<!-- <hello-screen v-if='modifiers.show_hello' id='hello-screen'></hello-screen> -->
			<!-- <sign-in id="sign-in"></sign-in> -->
		</div>
	</div>
</template>

<script>
 	import axios from 'axios';
 	export default {
		name: 'app',
		data: function () {
			return {
				msg: 'kek',
				modifiers: {
					show_vote: true,
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
		}
	}
</script>

