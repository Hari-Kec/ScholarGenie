import React, { useState } from 'react'
import Uploader from './components/Uploader'
import ChatBox from './components/ChatBox'
import ResponseView from './components/ResponseView'

function App() {
  const [response, setResponse] = useState("")
  return (
    <div className="app">
      <h1>ScholarGenie</h1>
      <Uploader />
      <ChatBox setResponse={setResponse} />
      <ResponseView response={response} />
    </div>
  )
}

export default App
