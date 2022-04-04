import React from 'react'
import './Navbar.css'

const Navbar = () => {
    return (
        <div className="container">
            <div className="logo">
                Todo-List
            </div>
            <div className="navitems">
                <a href="#">Главная</a>
                <a href="#">О нас</a>
            </div>
        </div>
    )
}

export default Navbar