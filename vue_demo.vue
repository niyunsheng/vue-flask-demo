<template>
    <div id="app">
        {{v1}} + {{v2}} = {{ans}}
        <button v-on:click="func_deom">
            计算
        </button>
    </div>
</template>

<script>
    var app = new Vue({
        el:"#app",
        data:{
            v1: 100,
            v2: 101,
            ans: ""
        },
        methods: {
            func_demo: function(event) {
                axios.get('/add?v1="v1"&v2="v2"')
                    .then(function (response) {
                        ans = response
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        }
    })
</script>

<style>
</style>
