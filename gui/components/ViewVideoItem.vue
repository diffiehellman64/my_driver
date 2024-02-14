<template>
  <v-overlay v-model="isOpen" class="align-center justify-center" persistent>
    <div class="d-flex justify-center">
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
    <VideoPlayer
      :video-path="props.video.upload"
      :quality="props.video.size"
      :poster="props.video.poster"
      :width="`${width}px`"
      height="400px"
      autoplay
    />
  </v-overlay>
</template>

<script setup lang="ts">
const isOpen: Ref = ref(false)
let dialogResolve: any = null
const width: Ref = ref(600)

const props = defineProps({
  video: {
    type: Object,
    default: () => {
      return {}
    },
    required: true,
  },
})

onMounted(() => {
  nextTick(() => {
    window.addEventListener('resize', onResize)
  })
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', onResize)
})

function onResize(e: any) {
  const w = e.target.innerWidth
  if (w < width.value) {
    width.value = w
  }
}

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
