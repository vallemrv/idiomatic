<template>
  <v-container>
       <login-user v-if="!user"></login-user>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue';
import LoginUser from '@/components/LoginUser.vue';
import { mapState } from 'vuex';
export default defineComponent({
  name: 'HomeView',
  components: {
    LoginUser,
},
computed:{
  ...mapState(["user"])
},
mounted(){
  console.log(localStorage.user)
  if (localStorage.user){
     this.$store.state.user = localStorage.user;
  }
}

});
</script>
