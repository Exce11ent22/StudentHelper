import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './verification-card.css'

const VerificationCard = (props) => {
  return (
    <div className="verification-card-verification-card">
      <div className="verification-card-container">
        <h1 className="verification-card-text">{props.heading}</h1>
        <span className="verification-card-text1">{props.text}</span>
      </div>
      <div className="verification-card-container1">
        <h1 className="verification-card-text2">{props.heading1}</h1>
        <Link
          to="/admin_verivication"
          className="verification-card-navlink button"
        >
          <span className="verification-card-text3">{props.text1}</span>
        </Link>
      </div>
    </div>
  )
}

VerificationCard.defaultProps = {
  text1: ' Рассмотреть заявку',
  text: 'ID Заявки: 123',
  heading1: '23.04.2022',
  heading: 'Иван Иванов',
}

VerificationCard.propTypes = {
  text1: PropTypes.string,
  text: PropTypes.string,
  heading1: PropTypes.string,
  heading: PropTypes.string,
}

export default VerificationCard
