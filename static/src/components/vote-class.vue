<template>
	<div>
		<div class="container my-3">
			<div class="embed-responsive embed-responsive-1by1 mx-auto">
				<iframe class="embed-responsive-item mw-50" src="https://www.yooying.com/tim_smd"></iframe>
			</div>
		</div>
			<div class="container mx-auto" v-for="item in classes">
				<div class="btn-group btn-group-toggle col-md-12 my-1 mx-auto" data-toggle="buttons">
					<label class="btn btn-primary col-md-4">
						<input type="radio" v-bind:name="'group_'+item.id" v-bind:id="'group_'+item.id+'_1'" autocomplete="off" value=1>{{ item.if_true }}
					</label>
					<label class="btn btn-info col-md-4">
						<input type="radio" v-bind:name="'group_'+item.id" v-bind:id="'group_'+item.id+'_2'" autocomplete="off" value=0>{{ item.if_false }}
					</label>
					<label class="btn btn-dark col-md-4">
						<input type="radio" v-bind:name="'group_'+item.id" v-bind:id="'group_'+item.id+'_3'" autocomplete="off" value=-1>Not sure
					</label>
				</div>
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
			this.get_classes()
		},
		props: {
		},
		methods: {
			get_classes: function () {
				axios.get('/api/classes')
				.then(response => {
					this.classes = response.data.classes
				})
				.catch(e => {
					this.errors.push(e)
				})
			},
			get_profile: function () {
				axios.get('/api/profile')
				.then(response => {
					this.profile_classes = response.data.classes
				})
				.catch(e => {
					this.errors.push(e)
				})
			},
			vote: function () {
				axios.post('/api/vote',{
					profile: this.current_profile,
					votes: this.votes
				})
				.then(response => {
					//
				})
			},
		}
	}
</script>