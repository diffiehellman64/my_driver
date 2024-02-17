type RequestParams = {
  url: string
  method: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'
  data?: object
  pending: Ref
  baseURL?: string
}

// type UserCreds = {
//   username: string
//   password: string
// }

// export const useApi = async (params: ApiParams) => {
//   const token = useCookie<string | null>('auth:token')
//   const headers = new Headers({
//     Authorization: `Token ${token.value}`,
//   } as HeadersInit)
//   const config = useRuntimeConfig()
//   params.pending.value = true
//   const data = await $fetch(params.url, {
//     method: params.method,
//     body: params.data,
//     baseURL: params.baseURL,
//     headers,
//   })
//   params.pending.value = false
//   return data
// }

// export function useApi(params: RequestParams) {
//   // const config = useRuntimeConfig()

//   return useFetch('/auth/login', {
//     method: params.method,
//     headers: { 'Content-Type': 'application/json' },
//     body,
//     baseURL: 'https://dummyjson.com',
//     watch: false,
//     immediate: false,
//   })
// }
