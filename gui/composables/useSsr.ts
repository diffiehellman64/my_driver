export const useSsr = (path: string, opts: object = {}) => {
  const config = useRuntimeConfig()
  let url = config.public.API_URL
  if (process.server) {
    url = config.private.API_URL
  }

  return useLazyFetch(path, {
    baseURL: url,
    ...opts,
  })
}
