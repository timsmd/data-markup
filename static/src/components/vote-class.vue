<template>
	<div>
		<iframe src="https://web.stagram.com/tim_smd" width="480" height="480"></iframe>
		<div v-for="item in classes">
			<input type="radio" v-bind:id="item.id" value="Один" v-bind:name="item.id+'_'">
			<label for="one">{{ item.if_true }}</label>
			<input type="radio" v-bind:id="item.id" value="Два" v-bind:name="item.id+'_'">
			<label for="two">{{ item.if_false }}</label>
			<br>
		</div>
	</div>
</template>
<script>
	import axios from 'axios'
	export default {
		name: 'vote-class',
		data: function () {
			return {
				classes: []
			}
		},
		created: function () {
			axios.get('/api/classes')
			.then(response => {
				this.classes = response.data.classes
			})
			.catch(e => {
				this.errors.push(e)
			})
		},
		props: {
		},
		methods: {
			get_profile: function () {
				axios.get('/api/profile')
				.then(response => {
					this.profile_classes = response.data.classes
				})
				.catch(e => {
					this.errors.push(e)
				})
			}

		}
	}
</script>