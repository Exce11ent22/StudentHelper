import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './question-card.css'

const QuestionCard = (props) => {
  return (
    <Link to="/question" className="">
      <div className={`question-card-blog-post-card ${props.rootClassName} `}>
        <div className="question-card-raiting">
          <button className="question-card-button button">
            <svg viewBox="0 0 1024 1024" className="question-card-icon">
              <path
                d="M170 512l342-342 342 342-62 60-238-238v520h-84v-520l-240 238z"
                className=""
              ></path>
            </svg>
          </button>
          <button className="question-card-button1 button">
            <svg viewBox="0 0 1024 1024" className="question-card-icon2">
              <path
                d="M854 512l-342 342-342-342 62-60 238 238v-520h84v520l240-238z"
                className=""
              ></path>
            </svg>
          </button>
          <span className="">{props.text}</span>
        </div>
        <div className="question-card-container">
          <div className="question-card-container1">
            <span className="question-card-text1">{props.label}</span>
            <span className="question-card-text2">{props.when}</span>
          </div>
          <h1 className="question-card-text3">{props.title}</h1>
        </div>
      </div>
    </Link>
  )
}

QuestionCard.defaultProps = {
  image_src: 'https://play.teleporthq.io/static/svg/default-img.svg',
  when: '23.04.2022',
  rootClassName: '',
  label: 'Мат. анализ',
  title: 'Помогите взять интеграл, пж',
  text: '+100500',
}

QuestionCard.propTypes = {
  image_src: PropTypes.string,
  when: PropTypes.string,
  rootClassName: PropTypes.string,
  label: PropTypes.string,
  title: PropTypes.string,
  text: PropTypes.string,
}

export default QuestionCard
