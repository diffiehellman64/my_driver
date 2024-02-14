<template>
  <div>
    <v-btn icon @click="toggleTheme()">
      <v-icon v-if="theme.global.name.value === 'light'">
        mdi-weather-night
      </v-icon>
      <v-icon v-else>mdi-white-balance-sunny</v-icon>
    </v-btn>
  </div>
</template>

<script setup lang="ts">
import { useTheme } from 'vuetify'

const theme = useTheme()

function toggleTheme() {
  theme.global.name.value === 'light'
    ? (theme.global.name.value = 'maria')
    : (theme.global.name.value = 'light')
}
</script>
