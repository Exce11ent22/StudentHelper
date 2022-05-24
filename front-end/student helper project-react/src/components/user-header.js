import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import UserNavigationLinks from './user-navigation-links'
import './user-header.css'

const UserHeader = (props) => {
  return (
    <header
      data-role="Header"
      className={`user-header-header ${props.rootClassName} `}
    >
      <div className="user-header-container">
        <Link to="/" className="user-header-navlink">
          <h1 className="user-header-text">{props.heading}</h1>
        </Link>
        <div className="user-header-nav">
          <UserNavigationLinks
            rootClassName="rootClassName12"
            className=""
          ></UserNavigationLinks>
        </div>
      </div>
      <div className="user-header-btn-group">
        <button className="user-header-button button">{props.button}</button>
      </div>
    </header>
  )
}

UserHeader.defaultProps = {
  rootClassName: '',
  button: 'Выход',
  heading: 'Student Helper',
}

UserHeader.propTypes = {
  rootClassName: PropTypes.string,
  button: PropTypes.string,
  heading: PropTypes.string,
}

export default UserHeader
