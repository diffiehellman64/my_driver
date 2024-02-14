<template>
  <v-menu
    v-model="show"
    :style="{ top: `${position.y}px`, left: `${position.x}px` }"
  >
    <v-list dense>
      <v-list-item
        v-for="(item, key) in props.menuItems"
        :key="key"
        @click="selected(item)"
      >
        <v-list-item-title>
          <v-icon left>mdi-{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script setup lang="ts">
import { MenuItem } from '~/composables/MenuItem'

const props = defineProps({
  menuItems: {
    type: Array<MenuItem>,
    required: true,
    default: () => [],
  },
})

const emit = defineEmits(['select'])

const show: Ref = ref(false)
const position: Ref = ref({
  x: null,
  y: null,
})

const selected = (item: MenuItem) => {
  emit('select', item)
}

const open = () => {
  show.value = true
}

const setPosition = (x: number, y: number) => {
  position.value = { x, y }
}

defineExpose({
  open,
  setPosition,
})
</script>
