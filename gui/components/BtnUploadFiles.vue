<template>
  <span>
    <v-btn icon="mdi-cloud-upload" @click="openExplorer()" />
    <input
      ref="explorer"
      class="d-none"
      type="file"
      multiple
      :loading="isLoading"
      @change="selected"
    />
  </span>
</template>

<script setup lang="ts">
const explorer: Ref = ref()
const isLoading: Ref = ref(false)

const emit = defineEmits(['update:preview', 'updateProgress'])

const props = defineProps({
  dirId: { type: Number, default: 0, require: true },
})

const openExplorer = () => {
  explorer.value.click()
}

const selected = (event: any) => {
  const previewImages = []
  const files = event.target.files
  for (let i = 0; i < files.length; i++) {
    previewImages.push({
      name: files[i].name,
      mime_type: files[i].type,
      size: files[i].size,
      lastModified: files[i].lastModifiedDate,
      upload: URL.createObjectURL(files[i]),
    })
    const formData = new FormData()
    formData.append('file', files[i])
    useUpload(
      `/api/wfs/item/${props.dirId}/upload/`,
      formData,
      function (progress: number) {
        emit('updateProgress', { index: i, progress })
      },
      function (obj: any) {
        emit('updateProgress', { index: i, progress: 101, obj })
      }
    )
  }
  emit('update:preview', previewImages)
}
</script>
