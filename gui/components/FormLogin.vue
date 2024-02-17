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

    <v-btn :loading="loading" color="primary" class="mb-3" @click="login"
      >Sing In</v-btn
    >
  </v-form>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/store/auth' // import the auth store we just created

const { auth } = useAuthStore() // use authenticateUser action from  auth store
const { authenticated, loading } = storeToRefs(useAuthStore()) // make authenticated state reactive with storeToRefs

const user = ref({
  username: 'kminchelle',
  password: '0lelplR',
})

const router = useRouter()
const authObj = useAuth(user.value)

const login = async () => {
  await auth(authObj)
  if (authenticated) {
    router.push('/') // redirect to homepage if user is authenticated
  }
}
</script>
