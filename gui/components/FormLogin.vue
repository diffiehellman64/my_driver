<template>
  <v-form class="d-flex flex-column auth-form">
    <v-text-field
      v-model="user.username"
      label="username"
      variant="outlined"
      density="compact"
      hide-details
      class="mb-3"
    />
    <v-text-field
      v-model="user.password"
      label="password"
      variant="outlined"
      density="compact"
      type="password"
      hide-details
      class="mb-5"
    />
    <v-btn color="primary" class="mb-3" @click="login">Sing In</v-btn>
    <v-btn @click="emit('replaceMe', 'registration')">Sing Up</v-btn>
  </v-form>
</template>

<script setup lang="ts">
const user: Ref = ref({})
const { signIn } = useAuth()
const emit = defineEmits(['replaceMe'])

const showMessage = inject('showMessage')

const login = async () => {
  try {
    await signIn(user.value, { callbackUrl: '/' })
  } catch (error) {
    showMessage(error)
  }
}
</script>
