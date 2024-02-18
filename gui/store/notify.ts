import { defineStore } from 'pinia'

type Message = {
  text: string
  show: boolean
}

type StateMessages = {
  messages: Message[]
}

export const useNotifyStore = defineStore('notify', {
  state: (): StateMessages => ({
    messages: [],
  }),

  actions: {
    async addMessage(msg: Message) {
      this.messages.push(msg)
    },

    removeMessage() {},
  },
})
