import React, { useState } from 'react'

function ChatBox({ setResponse }) {
  const [query, setQuery] = useState("")
  const [mode, setMode] = useState("summary")

  const ask = async () => {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, mode })
    })
    const data = await res.json()
    setResponse(data.response)
  }

  return (
    <div>
      <textarea onChange={(e) => setQuery(e.target.value)} />
      <select onChange={(e) => setMode(e.target.value)}>
        <option value="summary">Summary</option>
        <option value="eli5">Explain Like I'm 5</option>
        <option value="analogy">Analogy</option>
      </select>
      <button onClick={ask}>Ask</button>
    </div>
  )
}

export default ChatBox
