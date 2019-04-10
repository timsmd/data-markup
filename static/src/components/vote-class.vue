<template>
	<div>
		<p class="text-center">Profile:</p>
		<div class="container mb-3">
			<div class="embed-responsive embed-responsive-1by1 my-auto mx-auto">
				<iframe class="embed-responsive-item" v-bind:src="'https://www.yooying.com/'+current_profile"></iframe>
			</div>
		</div>
		<div class="container mx-auto">
			<div class="form-row text-center my-3" v-for="item in classes">
				<div class="btn-group btn-group-toggle col-sm-12 mx-auto">
					<label class="btn btn-primary col-md-6">
						<input type="radio"
						v-bind:name="'group_'+item.id"
						v-bind:id="'group_'+item.id+'_1'"
						autocomplete="off"
						value="1"
						v-model="votes[''+item.id]">{{ item.if_true }}
					</label>
					<label class="btn btn-info col-md-6">
						<input type="radio" 
						v-bind:name="'group_'+item.id"
						v-bind:id="'group_'+item.id+'_2'"
						autocomplete="off"
						v-model="votes[''+item.id]"
						value="0">{{ item.if_false }}
					</label>
					<label class="btn btn-dark col-md-6">
						<input type="radio"
						v-bind:name="'group_'+item.id"
						v-bind:id="'group_'+item.id+'_3'"
						autocomplete="off"
						v-model="votes[''+item.id]"
						value="-1">Not sure
					</label>
				</div>
			</div>
			<div class="form-row text-center my-3">
				<span>votes: {{votes}}</span>
				<div class="col-sm-12 mx-auto mb-4">
					<button type="button" class="btn btn-danger col-sm-12" @click="">Vote</button>
				</div>
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
				classes: [],
				current_profile: 'tim_smd',
				votes: {},
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