<template>
  <v-form class="d-flex flex-column auth-form">
    <v-text-field
      v-model="user.username"
      label="username"
      variant="outlined"
      density="compact"
      hide-details="auto"
      class="mb-3"
    />
    <v-text-field
      v-model="user.password"
      label="password"
      variant="outlined"
      density="compact"
      type="password"
      hide-details="auto"
      class="mb-3"
    />

    <v-text-field
      v-model="user.email"
      label="email"
      variant="outlined"
      density="compact"
      type="email"
      hide-details="auto"
      class="mb-5"
    />
    <v-btn color="primary" class="mb-3" @click="registration">Sing Up</v-btn>
    <v-btn @click="emit('replaceMe', 'login')">Sing In</v-btn>
  </v-form>
</template>

<script setup lang="ts">
const user: Ref = ref({})
const { signUp } = useAuth()
const emit = defineEmits(['replaceMe'])

function registration() {
  signUp(user.value, { callbackUrl: '/' })
}
</script>
