<template>
  <v-app-bar>
    <template #prepend>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
    </template>
    <v-app-bar-title>app</v-app-bar-title>
    <v-btn
      v-for="item in navItems"
      v-show="!item.hide"
      :key="item.path"
      :text="item.title"
      :to="item.path"
      :prepend-icon="item.icon"
      class="mr-2 no-radius"
      min-height="100%"
    />
    <btn-theme-change class="mr-3" />
  </v-app-bar>
</template>

<script setup lang="ts">
const navItems = computed(() => [
  { title: "Home", path: "/", icon: "mdi-home", hide: false },
  { title: "Dev", path: "/dev", icon: "mdi-tools" },
  // { title: "Login", path: "/login", icon: "mdi-login", hide: data.value?.id },
  { title: "Login", path: "/login", icon: "mdi-login" },
]);
</script>

<style scoped>
.no-radius {
  border-radius: 0;
}
</style>
