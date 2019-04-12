<template>
	<div>
		<div class="container mx-auto text-center">
			<button type="button" class="btn btn-outline-dark my-3 col-sm-6" @click="change_mode">Switch to {{ mode_name }}</button>
			<div class="form-row text-center">
				<div class="col-sm-6 mx-auto mt-3">
					<label for="validationCustomUsername">Username</label>
					<div class="input-group">
						<div class="input-group-prepend">
							<span class="input-group-text" id="input-at">@</span>
						</div>
						<input type="text" class="form-control" id="input-username" placeholder="Username" autocomplete="off" v-model="username">
						<div class="invalid-feedback d-block">
							{{ message }}
						</div>
					</div>
				</div>
			</div>
			<div class="form-row text-center">
				<div class="col-sm-6 mx-auto my-3">
						<label for="inputPassword">Password</label>
						<input type="password" class="form-control" id="inputPassword" placeholder="Password" autocomplete="off" v-model="password">
				</div>
			</div>
			<div class="form-row text-center">
				<div class="col-sm-6 mx-auto mb-4">
					<button v-if="mode === 1" type="button" class="btn btn-primary col-6" @click="login">Log In</button>
					<button v-if="mode === 2" type="button" class="btn btn-dark col-6" @click="signup">Sign Up</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';
	export default {
		name: 'sign-in',
		data: function () {
			return {
				message: '',
				username: '',
				password: '',
				errors: [],
				mode: 1,
				mode_name: 'Sign Up',
			}
		},
		methods: {
			change_mode: function () {
				if (this.mode === 1) {
					this.mode = 2;
					this.mode_name = 'Log In';
					return;
				}
				if (this.mode === 2) {
					this.mode = 1;
					this.mode_name = 'Sign Up';
					return;
				}
			},
			login: function () {
				if (this.username != '' && this.password != '') {
					axios.post('/api/login', {
						username: this.username,
						password: this.password
					})
					.then(response => {
						this.message = response.data.info;
						if (response.data.logged_in) {
							this.logged_in = true;
							this.current_user = response.data.username;
							this.$emit('loggedInState', { logged_in:true, current_user: this.username });
							this.$emit('redirect_route', 2);
						}
					})
					.catch(e => {
						this.errors.push(e)
					})
					return;
				}
				this.message = 'username and password must not be empty'
			},
			signup: function () {
				if (this.username != '' && this.password != '') {
					axios.post('/api/signup', {
						username: this.username,
						password: this.password
					})
					.then(response => {
						this.message = response.data.info;
						if (response.data.signed_up) {
							this.$emit('loggedInState', { logged_in:true, current_user: this.username });
							this.$emit('redirect_route', 2);
						}
					})
					.catch(error => {
						this.errors.push(error)
					})
					return;
				}
				this.message = 'username and password must not be empty'
			},
		}
	}
</script>
