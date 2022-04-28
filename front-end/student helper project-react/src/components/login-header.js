import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './login-header.css'

const LoginHeader = (props) => {
  return (
    <header
      data-role="Header"
      className={`login-header-header ${props.rootClassName} `}
    >
      <Link to="/" className="login-header-navlink">
        <h1 className="login-header-text">
          <span className="">Student Helper</span>
        </h1>
      </Link>
    </header>
  )
}

LoginHeader.defaultProps = {
  rootClassName: '',
}

LoginHeader.propTypes = {
  rootClassName: PropTypes.string,
}

export default LoginHeader
