<template>
    <div>
        <nav class="navbar navbar-light">
                <a class="navbar-brand text-light"
                @click="$emit('redirect_route', 2)"
                href=#
                v-if="login_info.logged_in">Hello, {{ login_info.current_user }}!</a>
                <a class="navbar-brand text-light"
                @click="$emit('redirect_route', 1)"
                href=#
                v-else="login_info.logged_in">Home</a>
                <button type="button" v-if="login_info.logged_in" class="btn btn-light" @click="logout">Logout</button>
                <button type="button" v-else="login_info.logged_in" class="btn btn-light" @click="$emit('redirect_route', 3)">Login</button>
        </nav>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'nav-bar',
        props: ['login_info'],
        data: function () {
            return {
                errors: []
            }
        },
        methods: {
            logout: function () {
                axios.get('/api/logout')
                .then(response => {
                    this.$cookies.remove('session_id')
                    this.message = response.data.logged_out;
                    this.$emit('loggedInState', { logged_in:false, current_user: '' });
                    this.$emit('redirect_route', 1);
                    this.$emit('reset_cookie')
                })
                .catch(e => {
                    this.errors.push(e)
                })
            },
        }
    }
</script>