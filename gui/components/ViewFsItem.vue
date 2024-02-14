<template>
  <div v-if="props.item" class="fs-item px-2 pt-2 rounded-lg" draggable="true">
    <v-img
      v-if="props.item.mime_type.split('/')[0] === 'image'"
      :src="item.size['100x100'] ? item.size['100x100'] : item.upload"
      :width="itemSize"
      :aspect-ratio="1"
      cover
      class="rounded-lg"
    >
      <template #placeholder>
        <v-row class="fill-height ma-0" align="center" justify="center">
          <v-progress-circular indeterminate color="grey-lighten-5" />
        </v-row>
      </template>
      <v-row
        v-if="props.item.progress"
        class="fill-height ma-0"
        align="center"
        justify="center"
      >
        <v-progress-circular color="grey-lighten-5">{{
          props.item.progress
        }}</v-progress-circular>
      </v-row>
    </v-img>

    <v-img
      v-else-if="props.item.mime_type.split('/')[0] === 'video'"
      :src="item.poster ? item.poster : item.upload"
      :width="itemSize"
      :aspect-ratio="1"
      cover
      class="rounded-lg"
    >
      <template #placeholder>
        <v-row class="fill-height ma-0" align="center" justify="center">
          <v-progress-circular indeterminate color="grey-lighten-5" />
        </v-row>
      </template>
      <v-row
        v-if="props.item.progress"
        class="fill-height ma-0"
        align="center"
        justify="center"
      >
        <v-progress-circular color="grey-lighten-5">{{
          props.item.progress
        }}</v-progress-circular>
      </v-row>
      <v-row align="center" justify="center" class="fill-height ma-0">
        <v-icon size="70">mdi-motion-play</v-icon>
      </v-row>
    </v-img>

    <v-icon v-else :size="itemSize">{{
      mimeIcons[props.item.mime_type]
    }}</v-icon>

    <div class="item-name">{{ props.item.name }}</div>
  </div>
</template>

<script setup lang="ts">
const itemSize = 100
const props = defineProps({
  item: { type: Object, required: true },
})

const mimeIcons: any = {
  dir: 'mdi-folder',
  'application/vnd.debian.binary-package': 'mdi-debian',
}
</script>

<style scoped>
.item-name {
  max-width: 100px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
