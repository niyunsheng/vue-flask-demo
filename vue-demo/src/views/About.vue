<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div id="add">
      {{v1}} + {{v2}} = {{ans}}
      <button v-on:click="func_demo()">
          计算
      </button>
    </div>
  </div>
  
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default{
  name: 'add',
  data(){
    return {
      v1:"100",
      v2:"200",
      ans:" "
    }
  },
  methods: {
    func_demo(){
      // alert("click");
      axios.get('http://localhost:5000/add',{
        params:{
          v1:this.v1,
          v2:this.v2
        }
      })
      .then(function (response) {
          alert(response);
          this.ans = response
      })
      .catch(function (error) {
          alert(error);
          console.log(error);
      });
    }
  }
}
  
</script>