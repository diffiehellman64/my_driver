<template>
  <v-app-bar>
    <template #prepend>
      <v-app-bar-nav-icon />
    </template>

    <v-app-bar-title>app</v-app-bar-title>

    <v-btn
      v-for="item in navItems"
      v-show="item.show"
      :key="item.path"
      :text="item.title"
      :to="item.path"
      :prepend-icon="item.icon"
      class="mr-2 menu-item"
    />

    <btn-theme-change v-if="authenticated" class="mr-3" />
    <!-- {{ authenticated }} -->
    <!-- {{ navItems }} -->
  </v-app-bar>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia' // import storeToRefs helper hook from pinia
import { useAuthStore } from '~/store/auth' // import the auth store we just created

const router = useRouter()
// const { logUserOut } = useAuthStore() // use authenticateUser action from  auth store
const { authenticated } = storeToRefs(useAuthStore()) // make authenticated state reactive with storeToRefs

// const navItems = computed(() => [
//   { title: 'Home', path: '/', icon: 'mdi-home', show: true },
//   { title: 'Dev', path: '/dev', icon: 'mdi-tools', show: true },
//   { title: 'Login', path: '/login', icon: 'mdi-login', show: !authenticated },
//   { title: 'Login', path: '/login', icon: 'mdi-login', show: true },
// ])

const navItems = ref([
  { title: 'Home', path: '/', icon: 'mdi-home', show: true },
  { title: 'Dev', path: '/dev', icon: 'mdi-tools', show: true },
  { title: 'Login', path: '/login', icon: 'mdi-login', show: !authenticated },
  // { title: 'Login', path: '/login', icon: 'mdi-login', show: true },
])

// const logout = () => {
//   logUserOut()
//   router.push('/login')
// }
</script>

<style scoped>
.menu-item {
  border-radius: 0;
  min-height: 100%;
}
</style>
