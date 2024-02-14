export const useUpload = (
  url: string,
  formData: FormData,
  onProgress: any,
  onReady: any
) => {
  const token = useCookie<string | null>('auth:token')
  const xhr = new XMLHttpRequest()
  const config = useRuntimeConfig()
  url = `${config.public.API_URL}${url}`
  xhr.open('post', url, true)
  xhr.setRequestHeader('Authorization', `Token ${token.value}`)
  xhr.upload.onprogress = function (e) {
    onProgress(Math.round((e.loaded / e.total) * 100))
  }
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      onReady(JSON.parse(xhr.responseText))
    }
  }
  xhr.send(formData)
}
