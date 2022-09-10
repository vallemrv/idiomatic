<template>
  <v-toolbar>
    <v-toolbar-title>IDIOMATIC</v-toolbar-title>
  </v-toolbar>
  <registro-user ></registro-user>
</template>

<script>
import { defineComponent } from 'vue';
import RegistroUser from '@/components/RegistroUser.vue';
export default defineComponent({
  name: 'HomeView',
  components: {
    RegistroUser,
},
});
</script>
