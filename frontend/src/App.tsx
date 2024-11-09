import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'



// import './App.css'

//components
import Navbar from './components/Navbar';
import Footer from './components/Footer';

// pages
import { Home } from './pages/Home';

function App() {

  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />} />
        </Routes>
        <Footer />
      </Router>
    </>
  )
}

export default App
