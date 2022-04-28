import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './answer-card.css'

const AnswerCard = (props) => {
  return (
    <div className="answer-card-answer-card">
      <div className="answer-card-user">
        <Link to="/profile" className="answer-card-navlink">
          <span>Петр Петров</span>
        </Link>
        <span className="answer-card-text01">
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
        <span>
          <span>Верифицирован</span>
        </span>
      </div>
      <div className="answer-card-answer">
        <div className="answer-card-raiting">
          <button className="answer-card-button button">
            <svg viewBox="0 0 1024 1024" className="answer-card-icon">
              <path d="M170 512l342-342 342 342-62 60-238-238v520h-84v-520l-240 238z"></path>
            </svg>
          </button>
          <button className="answer-card-button1 button">
            <svg viewBox="0 0 1024 1024" className="answer-card-icon2">
              <path d="M854 512l-342 342-342-342 62-60 238 238v-520h84v520l240-238z"></path>
            </svg>
          </button>
          <span>{props.text}</span>
        </div>
        <div className="answer-card-container">
          <span>
            <span>
              Чел ты... Это же изи! Учи мат. часть! Держи решение в
              прикрепленном файле! Какой-то текст. Какой-то текст. Какой-то
              текст. Какой-то текст. Какой-то текст. Какой-то текст. Какой-то
              текст. Какой-то текст.
            </span>
          </span>
          <div className="answer-card-files">
            <div className="answer-card-container1">
              <svg viewBox="0 0 1024 1024" className="answer-card-icon4">
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

AnswerCard.defaultProps = {
  link_text: 'https://example.com',
  text: '+100500',
  text1: 'https://studenthelper/file/1346134613',
}

AnswerCard.propTypes = {
  link_text: PropTypes.string,
  text: PropTypes.string,
  text1: PropTypes.string,
}

export default AnswerCard
