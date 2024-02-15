<template>
  <div class="d-block">
    <!-- <v-icon color="primary">mdi-home</v-icon> -->
    <v-btn @click="logout">sign out</v-btn>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/store/auth' // import the auth store we just created
definePageMeta({
  middleware: 'auth', // this should match the name of the file inside the middleware directory
})

const config = useRuntimeConfig()
const router = useRouter()

// const { status, data, signOut } = useAuth()
const { logUserOut } = useAuthStore()

function logout() {
  logUserOut()
  router.push('/login')
}
</script>
