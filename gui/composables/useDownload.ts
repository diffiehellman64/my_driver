export const useDownload = async (fileItem: any) => {
  const token = useCookie<string | null>('auth:token')
  const headers = new Headers({
    Authorization: `Token ${token.value}`,
  } as HeadersInit)

  const data = await $fetch(fileItem.upload, {
    headers,
  })

  const url = window.URL.createObjectURL(
    new Blob([data, { type: fileItem.mime_type }])
  )
  const link = document.createElement('a')
  link.href = url
  link.setAttribute('download', fileItem.name)
  document.body.appendChild(link)
  link.click()

  return data
}
