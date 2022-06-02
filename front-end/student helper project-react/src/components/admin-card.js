import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './admin-card.css'

const AdminCard = (props) => {
  return (
    <div className="admin-card-admin-card">
      <div className="admin-card-container">
        <h1 className="admin-card-text">{props.heading}</h1>
        <span className="admin-card-text1">{props.text}</span>
      </div>
      <div className="admin-card-container1">
        <Link to="/admin_change_role" className="admin-card-navlink button">
          {props.button}
        </Link>
        <button className="admin-card-button button">{props.button1}</button>
      </div>
    </div>
  )
}

AdminCard.defaultProps = {
  heading: 'Иван Иванов',
  text: 'Администратор',
  button1: 'Удалить',
  button: 'Изменить',
}

AdminCard.propTypes = {
  heading: PropTypes.string,
  text: PropTypes.string,
  button1: PropTypes.string,
  button: PropTypes.string,
}

export default AdminCard
