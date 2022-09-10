<template>
  <v-app>
    <v-toolbar app>
        <v-toolbar-title>IDIOMATIC</v-toolbar-title>
    </v-toolbar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
}
</script>
