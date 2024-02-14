<template>
  <v-snackbar v-model="show" multi-line location="top">
    {{ text }}
    <template #actions>
      <v-btn color="red" variant="text" @click="show = false"> Close </v-btn>
    </template>
  </v-snackbar>
</template>

<script setup lang="ts">
const show: Ref = ref(false)
const text: Ref = ref()

function open(t?: string) {
  show.value = true
  if (t) {
    text.value = t
  }
}

defineExpose({
  open,
})
</script>
