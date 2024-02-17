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

    <btn-logout v-if="authenticated" class="mr-3" />

    <btn-theme-change class="mr-3" />
  </v-app-bar>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useAuthStore } from '~/store/auth'

const { authenticated } = storeToRefs(useAuthStore()) // make authenticated state reactive with storeToRefs

const navItems = computed(() => [
  { title: 'Home', path: '/', icon: 'mdi-home', show: true },
  { title: 'Dev', path: '/dev', icon: 'mdi-tools', show: true },
  {
    title: 'Login',
    path: '/login',
    icon: 'mdi-login',
    show: !authenticated.value,
  },
])
</script>

<style scoped>
.menu-item {
  border-radius: 0;
  min-height: 100%;
}
</style>
