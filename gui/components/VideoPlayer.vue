<template>
  <div class="d-block">
    <div ref="player" :style="{ width: props.width, height: props.height }" />
  </div>
</template>

<script setup>
import Artplayer from 'artplayer'

const props = defineProps({
  videoPath: {
    type: String,
    default: '',
    required: true,
  },
  poster: {
    type: String,
    default: '',
    required: true,
  },
  width: { type: String, default: '600px', required: false },
  height: { type: String, default: '400px', required: false },
  autoplay: { type: Boolean, default: false, required: false },
  quality: {
    type: Object,
    default: () => {
      return []
    },
    required: false,
  },
})

const player = ref(null)
const qualitySelect = ref([])
onMounted(() => {
  nextTick(() => {
    // eslint-disable-next-line no-new
    new Artplayer({
      ...options,
      container: player.value,
    })
  })

  for (const q in props.quality) {
    qualitySelect.value.push({
      html: q,
      url: props.quality[q],
    })
  }
  qualitySelect.value[qualitySelect.value.length - 1].default = true
})

const options = reactive({
  container: '.artplayer-app',
  url: props.videoPath,
  poster: props.poster,
  volume: 0.5,
  isLive: false,
  muted: false,
  autoplay: props.autoplay,
  pip: true,
  autoSize: true,
  autoMini: true,
  // screenshot: true,
  // setting: true,
  loop: true,
  // flip: true,
  playbackRate: true,
  // aspectRatio: true,
  fullscreen: true,
  // fullscreenWeb: true,
  // subtitleOffset: true,
  miniProgressBar: true,
  mutex: true,
  backdrop: true,
  playsInline: true,
  autoPlayback: true,
  airplay: true,
  // theme: '#23ade5',
  // lang: navigator.language.toLowerCase(),
  // moreVideoAttr: {
  //   crossOrigin: 'anonymous',
  // },
  quality: qualitySelect.value,
  settings: [
    // {
    //   width: 200,
    //   html: 'Subtitle',
    //   tooltip: 'Bilingual',
    //   icon: 'mdi-play',
    //   selector: [
    //     {
    //       html: 'Display',
    //       tooltip: 'Show',
    //       switch: true,
    //       onSwitch: function (item) {
    //         item.tooltip = item.switch ? 'Hide' : 'Show'
    //         art.subtitle.show = !item.switch
    //         return !item.switch
    //       },
    //     },
    //     {
    //       default: true,
    //       html: 'Bilingual',
    //       url: '/assets/sample/subtitle.srt',
    //     },
    //     {
    //       html: 'Chinese',
    //       url: '/assets/sample/subtitle.cn.srt',
    //     },
    //     {
    //       html: 'Japanese',
    //       url: '/assets/sample/subtitle.jp.srt',
    //     },
    //   ],
    //   onSelect: function (item) {
    //     art.subtitle.switch(item.url, {
    //       name: item.html,
    //     })
    //     return item.html
    //   },
    // },
    // {
    //   html: 'Switcher',
    //   icon: '<img width="22" heigth="22" src="/state.svg">',
    //   tooltip: 'OFF',
    //   switch: false,
    //   onSwitch: function (item) {
    //     item.tooltip = item.switch ? 'OFF' : 'ON'
    //     console.info('You clicked on the custom switch', item.switch)
    //     return !item.switch
    //   },
    // },
    // {
    //   html: 'Slider',
    //   icon: '<img width="22" heigth="22" src="/state.svg">',
    //   tooltip: '5x',
    //   range: [5, 1, 10, 0.1],
    //   onRange: function (item) {
    //     return item.range + 'x'
    //   },
    // },
  ],

  // contextmenu: [
  //   {
  //     html: 'Custom menu',
  //     click: function (contextmenu) {
  //       console.info('You clicked on the custom menu')
  //       contextmenu.show = false
  //     },
  //   },
  // ],

  // layers: [
  //   {
  //     html: '<img width="100" src="/assets/sample/layer.png">',
  //     click: function () {
  //       window.open('https://aimu.app')
  //       console.info('You clicked on the custom layer')
  //     },
  //     style: {
  //       position: 'absolute',
  //       top: '20px',
  //       right: '20px',
  //       opacity: '.9',
  //     },
  //   },
  // ],
  // thumbnails: {
  //   url: '/assets/sample/thumbnails.png',
  //   number: 60,
  //   column: 10,
  // },
  // subtitle: {
  //   url: '/assets/sample/subtitle.srt',
  //   type: 'srt',
  //   style: {
  //     color: '#fe9200',
  //     fontSize: '20px',
  //   },
  //   encoding: 'utf-8',
  // },

  // highlight: [
  //   {
  //     time: 15,
  //     text: 'One more chance',
  //   },
  //   {
  //     time: 30,
  //     text: 'chapter_1',
  //   },
  //   {
  //     time: 45,
  //     text: 'chapter_2',
  //   },
  //   {
  //     time: 60,
  //     text: 'chapter_3',
  //   },
  //   {
  //     time: 75,
  //     text: 'chapter_4',
  //   },
  // ],

  // controls: [
  //   {
  //     position: 'right',
  //     html: 'Control',
  //     index: 1,
  //     tooltip: 'Control Tooltip',
  //     style: {
  //       marginRight: '20px',
  //     },
  //     click: function () {
  //       console.info('You clicked on the custom control')
  //     },
  //   },
  // ],
  // icons: {
  //   // loading: '<img src="/ploading.gif">',
  //   state: '<img width="150" heigth="150" src="/state.svg">',
  //   indicator: '<img width="16" heigth="16" src="/indicator.svg">',
  // },
})
</script>
