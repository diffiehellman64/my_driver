<template>
  <v-dialog v-model="isOpen" :width="`${width}`" persistent>
    <v-card elevation="3" class="px-5 py-5">
      <div
        class="d-flex justify-end mb-3"
        :class="{ 'justify-space-between': props.title }"
      >
        <v-card-title v-if="props.title" class="px-0 py-0 text-truncate">
          {{ props.title }}
        </v-card-title>
        <v-btn icon="mdi-close" density="comfortable" @click="close" />
      </div>
      <slot name="default" :apply="apply" />
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
const isOpen: Ref = ref(false)
let dialogResolve: any = null

const props = defineProps({
  title: { type: String, default: 'Dialog title', required: false },
  width: { type: String, default: '500', required: false },
})

const open = () => {
  const dialogPromise = new Promise((resolve) => {
    dialogResolve = resolve
  })
  isOpen.value = true
  return dialogPromise
}

const close = () => {
  dialogResolve(false)
  isOpen.value = false
}

const apply = (data: any) => {
  isOpen.value = false
  dialogResolve(data)
}

defineExpose({
  open,
})
</script>
