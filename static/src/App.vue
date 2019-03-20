<template>
  <div id="app">
	<h1>App says: {{ msg }}</h1>
  </div>
</template>

<script>
 	import axios from 'axios';

 	export default {
		name: 'app',
		data() {
			return {
				msg: ''
			}
		},
		created() {
			axios.get("/api/properties").then(r =>{
				this.msg = r.data.version
			})
		}
	}
</script>

