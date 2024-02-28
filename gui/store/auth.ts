import { defineStore } from 'pinia'
import { useNotifyStore } from './notify'

type StateAuth = {
  authenticated: boolean
  loading: boolean
  profile: any
  fetch: any
}

export const useAuthStore = defineStore('auth', {
  state: (): StateAuth => ({
    authenticated: false,
    loading: false,
    profile: {},
    fetch: {},
  }),

  actions: {
    init(body: UserCreds) {
      useAuthInit(body)
    },

    async auth(body: UserCreds) {
      const { data, pending, execute } = await useAuth(body)

      this.loading = true
      await execute()
      this.loading = false

      if (error.value) {
        addMessage({ text: 'Auth error', show: true })
      }

      if (data.value) {
        const token = useCookie('token')
        token.value = data.value.token
        this.profile = data.value
        this.authenticated = true
      }
    },

    logout() {
      const token = useCookie('token') // useCookie new hook in nuxt 3
      this.authenticated = false // set authenticated  state value to false
      token.value = null // clear the token cookie
    },
  },
})
