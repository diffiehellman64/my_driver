<template>
  <div>
    <v-snackbar
      v-for="msg in messages"
      v-model="msg.show"
      multi-line
      location="top"
    >
      {{ msg.text }}
      <template #actions>
        <v-btn color="red" variant="text" @click="msg.show = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script setup lang="ts">
import { useNotifyStore } from '~/store/notify'
const { messages } = storeToRefs(useNotifyStore())
</script>
