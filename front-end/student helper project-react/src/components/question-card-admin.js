import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './question-card-admin.css'

const QuestionCardAdmin = (props) => {
  return (
    <Link to="/admin_question">
      <div className="question-card-admin-question-card-admin">
        <div className="question-card-admin-raiting">
          <button className="question-card-admin-button button">
            <svg viewBox="0 0 1024 1024" className="question-card-admin-icon">
              <path d="M170 512l342-342 342 342-62 60-238-238v520h-84v-520l-240 238z"></path>
            </svg>
          </button>
          <button className="question-card-admin-button1 button">
            <svg viewBox="0 0 1024 1024" className="question-card-admin-icon2">
              <path d="M854 512l-342 342-342-342 62-60 238 238v-520h84v520l240-238z"></path>
            </svg>
          </button>
          <span>{props.text}</span>
        </div>
        <div className="question-card-admin-container">
          <div className="question-card-admin-container1">
            <span className="question-card-admin-text1">{props.text1}</span>
            <span className="question-card-admin-text2">{props.text2}</span>
            <button className="question-card-admin-button2 button">
              {props.button}
            </button>
          </div>
          <h1 className="question-card-admin-text3">{props.heading}</h1>
        </div>
      </div>
    </Link>
  )
}

QuestionCardAdmin.defaultProps = {
  heading: 'Помогите взять интеграл, пж',
  text: '+100500',
  button: 'Удалить',
  text1: 'Мат. анализ',
  text2: '23.04.2022',
}

QuestionCardAdmin.propTypes = {
  heading: PropTypes.string,
  text: PropTypes.string,
  button: PropTypes.string,
  text1: PropTypes.string,
  text2: PropTypes.string,
}

export default QuestionCardAdmin
