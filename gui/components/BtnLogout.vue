<template>
  <div>
    <v-btn icon @click="logOut()">
      <v-icon> mdi-logout </v-icon>
    </v-btn>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/store/auth'
const { logout } = useAuthStore()

const router = useRouter()

const logOut = () => {
  logout()
  router.push('/login')
}
</script>
