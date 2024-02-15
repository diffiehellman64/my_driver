<template>
  <div class="d-block">
    dev!!
    <!-- <client-only>
      {{ config }}
      <div>
        {{ status }}
      </div>
      <div>
        {{ data }}
      </div>
    </client-only>-->
    <v-btn @click="logout">sign out</v-btn>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/store/auth' // import the auth store we just created

const config = useRuntimeConfig()
const router = useRouter()

// const { status, data, signOut } = useAuth()
const { logUserOut } = useAuthStore()

function logout() {
  logUserOut()
  router.push('/login')
}
</script>
