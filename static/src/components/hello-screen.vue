<template>
	<div>
		<div class="container mx-auto" style="height: 250px;">
			<div class="row text-center">
				<div class="col-6 mx-auto mt-5">
					<button type="button" v-on:click="$emit('redirect_route', 3)" class="btn btn-primary col-6">Sign In</button>
				</div>
			</div>
			<div class="row">
				<div class="col-6 mx-auto my-2 text-center">
					<a href=# v-on:click="$emit('redirect_route', 2)">or vote without loggin in...</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'hello-screen',
		props: [],
		methods: {

		}
	}
</script>