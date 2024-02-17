type UserCreds = {
  username: string
  password: string
}

export function useAuth(body: UserCreds) {
  return useFetch('/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body,
    baseURL: 'https://dummyjson.com',
    watch: false,
    immediate: false,
  })
}
