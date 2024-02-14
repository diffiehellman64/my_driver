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
    </client-only>
    <v-btn @click="logout">sign out</v-btn> -->
  </div>
</template>

<script setup lang="ts">
const config = useRuntimeConfig();

// function logout() {
//   signOut({ callbackUrl: '/login' })
// }

// const { status, data, signOut } = useAuth()
</script>
