<template>
  <v-form v-if="item" v-model="isValid">
    <v-text-field
      v-model="item.name"
      label="Name"
      :rules="nameRules"
      variant="outlined"
      density="comfortable"
    />
    <v-btn :disabled="!isValid" :loading="isLoading" @click="saveItem">
      Save
    </v-btn>
  </v-form>
</template>

<script setup lang="ts">
const emit = defineEmits(['done'])

const props = defineProps({
  fsItem: {
    type: Object,
    default: () => {
      return {}
    },
    require: false,
  },
  parentId: { type: Number, default: 0, required: false },
})

const item: Ref = ref()
const isValid: Ref = ref()
const isLoading: Ref = ref(false)

onMounted(() => {
  item.value = JSON.parse(JSON.stringify(props.fsItem))
})

const nameRules = [(v: string) => !!v || 'Input name']

const saveItem = async () => {
  let data = null
  if (!item.value.id) {
    data = await useApi({
      url: '/api/wfs/item/',
      method: 'POST',
      data: {
        ...item.value,
        parent_dir_id: props.parentId,
        mime_type: 'dir',
      },
      pending: isLoading,
    })
  } else {
    data = await useApi({
      url: `api/wfs/item/${item.value.id}/`,
      method: 'PATCH',
      data: item.value,
      pending: isLoading,
    })
  }
  emit('done', data)
}
</script>
