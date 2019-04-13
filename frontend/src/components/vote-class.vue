<template>
    <div>
        <div class="row mt-2">
            <div class="col-6 mx-auto text-center">
                <p>
                    <a target="_blank" 
                    v-bind:href="current_profile.url">{{ current_profile.insta_username }}</a>
                    on Instagram
                </p>
            </div>
        </div>
        <div class="container mb-2">
            <div class="embed-responsive embed-responsive-4by3 col-sm-12 text-center wrap" style="min-width: 350px">
                <iframe
                v-if="isMobile()"
                class="embed-responsive-item"
                v-bind:src="current_profile.iframe_mobile"
                ></iframe>
                <iframe
                v-if="!isMobile()"
                class="embed-responsive-item"
                v-bind:src="current_profile.iframe_desktop"
                ></iframe>
            </div>
        </div>
        <div class="container mx-auto" style="max-width: 900px;">
            <div class="form-row text-center my-3" v-for="item in classes">
                <div class="btn-group btn-group-toggle col-sm-12 mx-auto">
                    <label class="btn btn-outline-primary col-md-6 btn-lg"
                     v-bind:class="{ active: votes[''+item.id]=='1'}">
                        <input type="radio"
                        v-bind:name="'group_'+item.id"
                        v-bind:id="'group_'+item.id+'_1'"
                        autocomplete="off"
                        value="1"
                        v-model="votes[''+item.id]">{{ item.if_true }}
                    </label>
                    <label class="btn btn-outline-info col-md-6 btn-lg"
                     v-bind:class="{ active: votes[''+item.id]=='0'}">
                        <input type="radio" 
                        v-bind:name="'group_'+item.id"
                        v-bind:id="'group_'+item.id+'_2'"
                        autocomplete="off"
                        v-model="votes[''+item.id]"
                        value="0">{{ item.if_false }}
                    </label>
                    <label class="btn btn-outline-dark col-md-6 btn-lg"
                     v-bind:class="{ active: votes[''+item.id]=='-1'}">
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
                <div class="col-sm-12 mx-auto mb-4">
                    <button 
                    type="button"
                    class="btn btn-danger col-sm-12 btn-lg"
                    v-bind:class="{disabled: !check_votes()}"
                    @click="vote">Vote</button>
                </div>
                <div class="col-sm-12 mx-auto mb-4">
                    <button 
                    type="button"
                    class="btn btn-light col-sm-12 btn-lg"
                    @click="skip">Skip</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios';
    import isMobile from '../util/isMobile';
    import getRandom from '../util/randomArrayElement';
    export default {
        name: 'vote-class',
        data: function () {
            return {
                classes: [],
                profiles: [],
                current_profile: {},
                votes: {},
            }
        },
        props: ['login_info'],
        created: function () {
            this.get_classes();
            this.get_profiles()
            .then(r => {
                this.current_profile = getRandom(this.profiles)
            })
        },
        methods: {
            isMobile: function () {
                return isMobile()
            },
            get_classes: function () {
                axios.get('/api/classes')
                .then(response => {
                    this.classes = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })
            },
            get_profiles: function () {
                return axios.get('/api/profiles')
                    .then(response => {
                        this.profiles = response.data;
                    })
                    .catch(e => {
                        this.errors.push(e)
                    })
            },
            check_votes: function () {
                return (Object.keys(this.votes).length == this.classes.length) ? true : false;
            },
            vote: function () {
                if (this.check_votes()) {
                    let current_votes = [];
                    for (let key in this.votes) {
                        current_votes.push({
                            class: Number(key),
                            value: Number(this.votes[key]),
                        })
                    }
                    axios.post('/api/vote',{
                        profile: this.current_profile.id,
                        votes: current_votes,
                    })
                    .then(response => {
                        this.profiles.splice(this.current_profile.index);
                        this.current_profile = getRandom(this.profiles)
                        this.votes = {};
                    })      
                }
            },
            skip: function () {
                this.current_profile = getRandom(this.profiles)
                this.votes = {};
            }
        }
    }
</script>

<style type="text/css">
    .wrap {
        width: 100%;
        height: 100%;
        min-height: 400px;
        max-height: 500px;
        position: relative;
        right: 0;
        bottom: 0;
        left: 0;
        top: 0;
        -webkit-overflow-scrolling: touch !important;
        overflow-y: auto !important;
        border: 2px solid #ddd;
        margin-bottom: 20px;
    }

    iframe {
        width: 100%;
        height: 100%;
        border: none;
        display: block;
        position: absolute;
    }
</style>