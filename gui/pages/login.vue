<template>
  <div class="d-flex align-center justify-center height-all">
    <!-- <div class="d-flex flex-column justify-center">
      <form-login v-if="form == 'login'" @replace-me="replaceComponent" />
      <form-registration
        v-if="form == 'registration'"
        @replace-me="replaceComponent"
      />
    </div> -->
  </div>
</template>

<script setup lang="ts">
// definePageMeta({
//   layout: 'empty',
//   auth: {
//     unauthenticatedOnly: true,
//     navigateAuthenticatedTo: '/',
//   },
// })
// const form: Ref = ref('login')

// function replaceComponent(comp: string) {
//   form.value = comp
// }
</script>

<style scoped>
.height-all {
  height: 90vh;
}

.auth-form {
  width: 300px;
}
</style>
