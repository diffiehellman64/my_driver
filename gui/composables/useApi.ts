type ApiParams = {
  url: string
  method: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'
  data?: object
  pending: Ref
}

export const useApi = async (params: ApiParams) => {
  const token = useCookie<string | null>('auth:token')
  const headers = new Headers({
    Authorization: `Token ${token.value}`,
  } as HeadersInit)
  const config = useRuntimeConfig()
  params.pending.value = true
  const data = await $fetch(params.url, {
    method: params.method,
    body: params.data,
    baseURL: config.public.API_URL,
    headers,
  })
  params.pending.value = false
  return data
}
