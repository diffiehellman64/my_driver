<template>
  <div>
    <v-btn icon @click="logout()">
      <v-icon> mdi-logout </v-icon>
    </v-btn>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/store/auth'
const { logUserOut } = useAuthStore()

const router = useRouter()

const logout = () => {
  logUserOut()
  router.push('/login')
}
</script>
