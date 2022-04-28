import React from 'react'

import PropTypes from 'prop-types'

import './liderboard-card.css'

const LiderboardCard = (props) => {
  return (
    <div className="liderboard-card-liderboard-card">
      <div className="liderboard-card-container">
        <h1 className="liderboard-card-text">{props.heading}</h1>
        <span className="liderboard-card-text1">{props.text}</span>
      </div>
      <div className="liderboard-card-container1">
        <h1 className="liderboard-card-text2">{props.heading1}</h1>
        <h1 className="liderboard-card-text3">{props.heading2}</h1>
      </div>
    </div>
  )
}

LiderboardCard.defaultProps = {
  heading: 'Иван Иванов',
  heading2: 'Прирост: +57',
  heading1: 'Рейтинг: 357',
  text: 'Воронежский Государственный Университет',
}

LiderboardCard.propTypes = {
  heading: PropTypes.string,
  heading2: PropTypes.string,
  heading1: PropTypes.string,
  text: PropTypes.string,
}

export default LiderboardCard
