import { useState } from 'react'
import './App.scss'
import HomePage from './home-page/homepage'
import NotifForm from './home-page/notif-form'
import Search from './home-page/search-form'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <header>
        <span>Flight Tracker</span>
      </header>
      <div className="home">
        <div id='main'>
          <HomePage />
        </div>
      </div>
      <div id="setnotif">
        <NotifForm />
      </div>
      <div id="search">
        <Search />
      </div>
    </>

  )
}

export default App
