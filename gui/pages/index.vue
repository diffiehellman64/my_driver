<template>
  <div class="d-block">
    <!-- <v-icon color="primary">mdi-home</v-icon> -->
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/store/auth' // import the auth store we just created

const config = useRuntimeConfig()
const router = useRouter()

// const { status, data, signOut } = useAuth()
</script>
