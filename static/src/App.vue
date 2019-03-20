<template>
	<div id="app">
		<h1>App says: {{ postInput }}</h1>
		<input v-model="postInput" placeholder="input text">
		<button v-on:click="postButton"> Press</button>
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
				errors: []
			}
		},
		created() {
			axios.get("/api/properties").then(r =>{
				this.msg = r.data.inputForm
			})
		},
		methods: {
			postButton : function () {
				axios.post('/api', {
					data: this.postInput
				})
				.then(response => {})
				.catch(e => {
					this.errors.push(e)
				})
			}
		}
	}
</script>

