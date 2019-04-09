<template>
	<div>
			<div class="form-row">
				<div class="col-md-4 mb-3">
					<label for="validationCustomUsername">Username</label>
					<div class="input-group">
						<div class="input-group-prepend">
							<span class="input-group-text" id="input-at">@</span>
						</div>
						<input type="text" class="form-control" id="input-username" placeholder="Username">
						<div class="invalid-feedback d-block">
							{{ message }}
						</div>
					</div>
				</div>
			</div>
			<div class="form-row">
				<div class="col-md-4 mb-3">
						<label for="inputPassword">Password</label>
						<input type="password" class="form-control" id="inputPassword" placeholder="Password">
				</div>
			</div>
			
	</div>
</template>

<script>
	export default {
		name: 'sign-in',
		data: function () {
			return {
				message: '',
			}
		}
	}
</script>
