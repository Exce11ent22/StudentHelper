import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import AdminNavigationLinks from './admin-navigation-links'
import './admin-header.css'

const AdminHeader = (props) => {
  return (
    <header
      data-role="Header"
      className={`admin-header-admin-header ${props.rootClassName} `}
    >
      <div className="admin-header-container">
        <Link to="/" className="admin-header-navlink">
          <h1 className="admin-header-text">{props.heading}</h1>
        </Link>
        <div className="admin-header-nav">
          <AdminNavigationLinks className=""></AdminNavigationLinks>
        </div>
      </div>
      <div className="admin-header-btn-group">
        <button className="admin-header-button button">{props.button}</button>
      </div>
    </header>
  )
}

AdminHeader.defaultProps = {
  rootClassName: '',
  button: 'Выход',
  heading: 'Student Helper',
}

AdminHeader.propTypes = {
  rootClassName: PropTypes.string,
  button: PropTypes.string,
  heading: PropTypes.string,
}

export default AdminHeader
