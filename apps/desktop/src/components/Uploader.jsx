import React from 'react'

function Uploader() {
  const handleUpload = async (e) => {
    const file = e.target.files[0]
    const formData = new FormData()
    formData.append("file", file)

    const res = await fetch("http://localhost:8000/parse", {
      method: "POST",
      body: formData
    })
    const data = await res.json()
    console.log(data.text)
  }

  return <input type="file" onChange={handleUpload} />
}

export default Uploader
