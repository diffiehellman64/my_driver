<template>
  <div
    class="d-block"
    @drop.prevent="onDrop"
    @dragenter.prevent="dragEnter = true"
    @dragleave.prevent="dragEnter = false"
  >
    <v-progress-circular
      v-if="isLoading"
      :size="70"
      :width="7"
      color="primary"
      indeterminate
      class="mx-auto mt-10"
    />
    <div v-else>
      <!-- <div class="d-flex justify-space-between"> -->
      <div>
        <h1>{{ dir.name }}</h1>
        <div>
          <v-btn
            icon="mdi-folder-home"
            :disabled="!dir.parent_dir_id"
            class="mx-2"
            @click="openDir(0)"
          />
          <v-btn
            icon="mdi-folder-upload"
            :disabled="!dir.parent_dir_id"
            class="mx-2"
            @click="openDir(dir.parent_dir_id)"
          />
          <v-btn icon="mdi-folder-plus" class="mx-2" @click="createNewDir" />
          <btn-upload-files
            v-model:preview="preview"
            :dir-id="dir.id"
            class="mx-2"
            @update-progress="updateProgress"
          />
        </div>
      </div>

      <div class="d-flex flex-wrap mt-3">
        <view-fs-item
          v-for="(item, key) in fsItems"
          v-show="item.progress != 101"
          :key="key"
          :item="item"
          class="mr-1 mb-1"
          :class="{ 'bg-primary': selectedItems.includes(item) }"
          @drop="drop(item)"
          @dragstart="dragstart(item)"
          @click="selectItem($event, item)"
          @dblclick="exec(item, key)"
          @contextmenu.prevent="showContextMenu($event, item, key)"
        />
      </div>
    </div>
    <context-menu ref="menu" :menu-items="menuItems" @select="selected" />

    <async-dialog ref="itemDialog" v-slot="{ apply }" :title="dialogTitle">
      <form-fs-item
        :parent-id="dir.id"
        :fs-item="selectedFsItem"
        @done="apply"
      />
    </async-dialog>

    <view-image-item
      ref="imageOverlay"
      :image="selectedFsItem"
      @next="nextImage"
      @previos="previosImage"
    />

    <view-video-item ref="videoOverlay" :video="selectedFsItem" />
  </div>
</template>

<script setup lang="ts">
import { MenuItem } from '~/composables/MenuItem'

const events = ['dragenter', 'dragover', 'dragleave', 'drop']

const selectedFsItemIndex: Ref = ref(0)
const selectedFsItem: Ref = ref()
const isLoading: Ref = ref(false)
const dir: Ref = ref({})
const itemDialog: Ref = ref()
const imageOverlay: Ref = ref()
const videoOverlay: Ref = ref()
const menu: Ref = ref()
const dialogTitle: Ref = ref('New directory')
const preview: Ref = ref([])
const dragEnter: Ref = ref(false)
const selectedItems: Ref = ref([])

const route = useRoute()
const router = useRouter()

const fsItems = computed(() => {
  if (dir.value.children) {
    return [...dir.value.children, ...preview.value]
  }
  return []
})

const menuItems = computed(() => {
  const items = [
    // { title: 'Select', icon: 'select' },
    { title: 'Delete', icon: 'delete' },
  ]

  if (selectedItems.value.length === 1) {
    return [
      { title: 'Open', icon: 'folder-open' },
      { title: 'Edit', icon: 'pencil' },
      ...items,
    ]
  }
  return [{ title: 'Unselect', icon: 'selection-remove' }, ...items]
})

// let dirId: Number = 0
// if (route.query.dir_id) {
//   dirId = +route.query.dir_id
// }
// const { data, pending } = await useSsr(`/api/wfs/item/${dirId}/`)
// watch(data, (val) => {
//   dir.value = val
// })

onMounted(() => {
  let dirId: Number = 0
  if (route.query.dir_id) {
    dirId = +route.query.dir_id
  }
  openDir(dirId)
  events.forEach((eventName: any) => {
    document.body.addEventListener(eventName, preventDefaults)
  })
})

onUnmounted(() => {
  events.forEach((eventName: any) => {
    document.body.removeEventListener(eventName, preventDefaults)
  })
})

const createNewDir = async () => {
  selectedFsItem.value = {}
  const newDir = await itemDialog.value.open()
  if (newDir) {
    dir.value.children.push(newDir)
  }
}

const selectItem = (event: any, item: any) => {
  if (selectedItems.value.includes(item)) {
    selectedItems.value = selectedItems.value.filter(
      (i: any) => i.id !== item.id
    )
    return
  }
  if (event.ctrlKey) {
    selectedItems.value.push(item)
  } else {
    selectedItems.value = [item]
  }
}

const exec = (item: any, index: number) => {
  if (item.mime_type === 'dir') {
    openDir(item.id)
  } else if (item.mime_type.split('/')[0] === 'image') {
    showImage(item, index)
  } else if (item.mime_type.split('/')[0] === 'video') {
    showVideo(item, index)
  } else {
    downloadFile(item)
  }
}

const openDir = async (dirId: Number) => {
  dir.value = await useApi({
    url: `/api/wfs/item/${dirId}/`,
    method: 'GET',
    pending: isLoading,
  })
  router.push({
    query: {
      dir_id: dir.value.id,
    },
  })
}

const showImage = async (imageItem: any, index: number) => {
  selectedFsItem.value = imageItem
  selectedFsItemIndex.value = index
  await imageOverlay.value.open()
}

const showVideo = async (videoItem: any, index: number) => {
  selectedFsItem.value = videoItem
  selectedFsItemIndex.value = index
  await videoOverlay.value.open()
}

const nextImage = () => {
  selectedFsItemIndex.value++
  if (dir.value.children.length === selectedFsItemIndex.value) {
    selectedFsItemIndex.value = 0
  }
  const fileItem = dir.value.children[selectedFsItemIndex.value]
  if (fileItem.mime_type.includes('image')) {
    selectedFsItem.value = fileItem
  } else {
    nextImage()
  }
}

const previosImage = () => {
  selectedFsItemIndex.value--
  if (selectedFsItemIndex.value < 0) {
    selectedFsItemIndex.value = dir.value.children.length - 1
  }
  const fileItem = dir.value.children[selectedFsItemIndex.value]
  if (fileItem.mime_type.includes('image')) {
    selectedFsItem.value = fileItem
  } else {
    previosImage()
  }
}

const downloadFile = (fileItem: any) => {
  useDownload(fileItem)
}

const showContextMenu = (e: any, item: any, index: number) => {
  menu.value.setPosition(e.clientX, e.clientY)
  menu.value.open()
  selectedFsItem.value = item
  selectedFsItemIndex.value = index
  if (!selectedItems.value.includes(item)) {
    selectedItems.value.push(item)
  }
}

const updateProgress = (p: any) => {
  preview.value[p.index].progress = p.progress
  if (p.progress === 101) {
    dir.value.children.push(p.obj[0])
  }
}

const selected = async (item: MenuItem) => {
  if (item.title === 'Open') {
    exec(selectedFsItem.value, selectedFsItemIndex.value)
    selectedItems.value = []
  } else if (item.title === 'Delete') {
    // if item not preview
    if (selectedFsItem.value.id) {
      const deletedItemsIds: any = await useApi({
        url: '/api/wfs/item/destroy_multi/',
        method: 'DELETE',
        pending: isLoading,
        data: { ids: selectedItems.value.map((i: any) => i.id) },
      })
      dir.value.children = dir.value.children.filter(
        (i: any) => !deletedItemsIds.includes(i.id)
      )
    } else {
      preview.value.splice(selectedFsItemIndex.value, 1)
    }
    selectedItems.value = []
  } else if (item.title === 'Edit') {
    dialogTitle.value = 'Rename directory'
    const updatedItem = await itemDialog.value.open()
    if (updatedItem) {
      dir.value.children[selectedFsItemIndex.value] = updatedItem
    }
    selectedItems.value = []
  } else if (item.title === 'Unselect') {
    // selectedItems.value.push(selectedFsItem.value)
    selectedItems.value = selectedItems.value.filter(
      (i: any) => selectedFsItem.value.id !== i.id
    )
  }
}

async function moveItems(items: any, newDir: any) {
  const movedIds: any = await useApi({
    url: `/api/wfs/item/${newDir.id}/absorb/`,
    method: 'PUT',
    pending: isLoading,
    data: { ids: items.map((i: any) => i.id) },
  })
  dir.value.children = dir.value.children.filter(
    (i: any) => !movedIds.includes(i.id)
  )
}

function preventDefaults(e: any) {
  e.preventDefault()
}

function drop(item: any) {
  if (item.mime_type === 'dir') {
    moveItems(selectedItems.value, item)
  }
}

function dragstart(item: any) {
  if (selectedItems.value.length > 0 && !selectedItems.value.includes(item)) {
    selectedItems.value.push(item)
  } else if (selectedItems.value.length === 0) {
    selectedItems.value = [item]
  }
}

const onDrop = (e: any) => {
  dragEnter.value = false
  const previewImages = []
  const files = e.dataTransfer.files
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
      `/api/wfs/item/${dir.value.id}/upload/`,
      formData,
      function (progress: number) {
        updateProgress({ index: i, progress })
      },
      function (obj: any) {
        updateProgress({ index: i, progress: 101, obj })
      }
    )
  }
  preview.value = previewImages
}
</script>
