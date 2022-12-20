import React from 'react'
import { Link } from 'react-router-dom'
import Logo from './Logo.gif'
import './style.css'
import bg from './loop.gif'

const style={
  backgroundImage: `url(${bg})`,
  backgroundPosition: 'center',
  backgroundSize: 'cover',
  backgroundRepeat: 'no-repeat',
  height: '100%',
  padding:'0px',
  margin:'0px !important'
}
const Welcom = () => {
  return (
    <div style={style}>
        <img src={Logo} style={{position:'relative',bottom:'25rem',right:'-17rem'}}></img>
        <center>
            <a href='main' style={{position:'relative',bottom:'45rem',right:'0rem'}}>Enter</a>
        </center>
    </div>
  )
}

export default Welcom