<template>
  <div class="d-block">
    <v-icon color="primary">mdi-home</v-icon>
  </div>
</template>

<script setup lang="ts">
  definePageMeta ({
    middleware: 'auth' // this should match the name of the file inside the middleware directory 

})
</script>
