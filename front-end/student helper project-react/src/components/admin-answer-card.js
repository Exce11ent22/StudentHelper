import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './admin-answer-card.css'

const AdminAnswerCard = (props) => {
  return (
    <div className="admin-answer-card-admin-answer-card">
      <div className="admin-answer-card-user">
        <Link to="/profile" className="admin-answer-card-navlink">
          <span>Петр Петров</span>
        </Link>
        <span className="admin-answer-card-text01">
          <span>
            20:24
            <span
              dangerouslySetInnerHTML={{
                __html: ' ',
              }}
            />
          </span>
          <span>24.04.2022</span>
          <span></span>
        </span>
        <span className="admin-answer-card-text05">
          <span>Верифицирован</span>
        </span>
        <button className="admin-answer-card-button button">
          {props.button}
        </button>
      </div>
      <div className="admin-answer-card-answer">
        <div className="admin-answer-card-raiting">
          <button className="admin-answer-card-button1 button">
            <svg viewBox="0 0 1024 1024" className="admin-answer-card-icon">
              <path d="M170 512l342-342 342 342-62 60-238-238v520h-84v-520l-240 238z"></path>
            </svg>
          </button>
          <button className="admin-answer-card-button2 button">
            <svg viewBox="0 0 1024 1024" className="admin-answer-card-icon2">
              <path d="M854 512l-342 342-342-342 62-60 238 238v-520h84v520l240-238z"></path>
            </svg>
          </button>
          <span>{props.text}</span>
        </div>
        <div className="admin-answer-card-container">
          <span>
            <span>
              Чел ты... Это же изи! Учи мат. часть! Держи решение в
              прикрепленном файле! Какой-то текст. Какой-то текст. Какой-то
              текст. Какой-то текст. Какой-то текст. Какой-то текст. Какой-то
              текст. Какой-то текст.
            </span>
          </span>
          <div className="admin-answer-card-files">
            <div className="admin-answer-card-container1">
              <svg viewBox="0 0 1024 1024" className="admin-answer-card-icon4">
                <path d="M554 384h236l-236-234v234zM256 86h342l256 256v512q0 34-26 59t-60 25h-512q-34 0-60-25t-26-59l2-684q0-34 25-59t59-25z"></path>
              </svg>
              <a
                href={props.link_text}
                target="_blank"
                rel="noreferrer noopener"
              >
                {props.text1}
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

AdminAnswerCard.defaultProps = {
  button: 'Удалить',
  link_text: 'https://example.com',
  text: '+100500',
  text1: 'file.jpg',
}

AdminAnswerCard.propTypes = {
  button: PropTypes.string,
  link_text: PropTypes.string,
  text: PropTypes.string,
  text1: PropTypes.string,
}

export default AdminAnswerCard
