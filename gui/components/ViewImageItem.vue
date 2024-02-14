<template>
  <v-overlay v-model="isOpen" class="align-center justify-center" persistent>
    <div class="d-flex justify-center overlay">
      <v-btn
        icon="mdi-arrow-left-bold"
        class="mb-3 mr-3"
        @click="emit('previos')"
      />
      <v-btn
        icon="mdi-arrow-right-bold"
        class="mb-3 mr-3"
        @click="emit('next')"
      />
      <v-btn icon="mdi-close" class="mb-3 mr-3" @click="close" />
    </div>

    <v-img
      v-touch="{
        left: () => emit('next'),
        right: () => emit('previos'),
      }"
      height="90vh"
      :src="props.image.upload"
      class="d-flex justify-end"
      width="90vw"
    >
      <template #placeholder>
        <v-row class="fill-height ma-0" align="center" justify="center">
          <v-progress-circular indeterminate color="grey-lighten-5" />
        </v-row>
      </template>
    </v-img>
  </v-overlay>
</template>

<script setup lang="ts">
const isOpen: Ref = ref(false)
let dialogResolve: any = null

const props = defineProps({
  image: {
    type: Object,
    default: () => {
      return {}
    },
    required: true,
  },
})

const emit = defineEmits(['next', 'previos'])

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

// const apply = (data: any) => {
//   isOpen.value = false
//   dialogResolve(data)
// }

defineExpose({
  open,
})
</script>

<style>
.overlay {
  position: absolute;
  width: 100%;
  top: 25px;
  right: 10px;
  z-index: 100000;
}
</style>
