import { defineStore } from 'pinia'
// import { useMessageStore } from '~/store/message'
// const { addMessage } = useMessageStore() // use authenticateUser action from  auth store
// import type { AsyncData, UseFetchOptions } from 'nuxt/app'
// import { useRequestHeaders } from 'nuxt/app'
// import { FetchError } from 'ofetch'

type UserCreds = {
  username: string
  password: string
}

type StateAuth = {
  authenticated: boolean
  loading: boolean
}

export const useAuthStore = defineStore('auth', {
  state: (): StateAuth => ({
    authenticated: false,
    loading: false,
  }),

  actions: {
    async auth(body: UserCreds) {
      const { data, pending, execute } = await useAuth(body)
      this.loading = true
      await execute()
      this.loading = false

      if (data.value) {
        const token = useCookie('token')
        token.value = data.value.token
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
