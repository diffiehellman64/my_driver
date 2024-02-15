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
    <!-- <v-btn @click="emit('replaceMe', 'registration')">Sing Up</v-btn> -->
    {{ user }}
  </v-form>
</template>

<script setup lang="ts">
// const user: Ref = ref({})
// const { signIn } = useAuth()
// const emit = defineEmits(['replaceMe'])

// const showMessage = inject('showMessage')

// const login = async () => {
//   // try {
//   //   await signIn(user.value, { callbackUrl: '/' })
//   // } catch (error) {
//   //   showMessage(error)
//   // }
// }

import { storeToRefs } from 'pinia' // import storeToRefs helper hook from pinia
import { useAuthStore } from '~/store/auth' // import the auth store we just created

const { authenticateUser } = useAuthStore() // use authenticateUser action from  auth store

const { authenticated } = storeToRefs(useAuthStore()) // make authenticated state reactive with storeToRefs

const user = ref({
  username: 'kminchelle',
  password: '0lelplR',
})
const router = useRouter()

const login = async () => {
  await authenticateUser(user.value) // call authenticateUser and pass the user object
  // redirect to homepage if user is authenticated
  if (authenticated) {
    router.push('/')
  }
}
</script>
