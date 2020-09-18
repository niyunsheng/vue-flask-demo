<template>
  <div class="about">
    <h1>This is an sample calculator</h1>
    <div v-on:input="func_demo()">
      <input v-model="v1" placeholder="edit me"/>
      <select v-model="operate" >
            <option value ="+">+</option>
            <option value ="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
      <input v-model="v2" placeholder="edit me"/>
      = {{ans}}
    </div>
  </div>
  
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default{
  data(){
    return {
      v1:"1",
      v2:"1",
      operate:"+",
      ans:"2"
    }
  },
  methods: {
    func_demo(){
      // alert("click");
      axios.get('http://localhost:5000/add',{
        params:{
          v1:this.v1,
          v2:this.v2,
          operate:this.operate
        }
      })
      .then((response)=>{
        console.log(response)
        this.ans = response.data;
      })
      .catch((error)=>{
        alert(error);
        console.log(error);
      });
    }
  }
}
  
</script>