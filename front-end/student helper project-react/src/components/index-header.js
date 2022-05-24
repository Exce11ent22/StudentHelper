import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './index-header.css'

const IndexHeader = (props) => {
  return (
    <header
      data-role="Header"
      className={`index-header-header ${props.rootClassName} `}
    >
      <div className="index-header-container">
        <Link to="/" className="index-header-navlink">
          <h1 className="index-header-text">
            <span className="">Student Helper</span>
          </h1>
        </Link>
      </div>
      <div className="index-header-btn-group">
        <Link to="/login" className="index-header-navlink1 button">
          <span className="">
            <span className="">Вход</span>
          </span>
        </Link>
      </div>
    </header>
  )
}

IndexHeader.defaultProps = {
  rootClassName: '',
}

IndexHeader.propTypes = {
  rootClassName: PropTypes.string,
}

export default IndexHeader
