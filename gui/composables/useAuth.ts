type UserCreds = {
  username: string
  password: string
}

let auth: any = {}

const init = (body: UserCreds) => {
  auth = useFetch('/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body,
    baseURL: 'https://dummyjson.com',
    immediate: false,
    watch: false,
  })
}

export async function useAuth(body: UserCreds) {
  if (!auth.execute) {
    init(body)
  }
  return auth
}
