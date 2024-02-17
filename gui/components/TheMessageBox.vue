<template>
  <!-- <v-alert
    v-for="msg in messages"
    :key="msg.text"
    :text="msg.text"
    class="alert"
  /> -->
</template>

<script setup lang="ts">
// const props = defineProps({
//   text: { type: String, default: null, require: true },
// })
// import { useMessageStore } from '~/store/message'
// const { messages } = storeToRefs(useMessageStore())
</script>

<style scoped>
.alert {
  position: absolute;
  right: 70px;
}
</style>
