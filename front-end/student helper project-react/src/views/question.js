import React from 'react'

import { Helmet } from 'react-helmet'

import UserHeader from '../components/user-header'
import AnswerCard from '../components/answer-card'
import Footer from '../components/footer'
import './question.css'

const Question = (props) => {
  return (
    <div className="question-container">
      <Helmet>
        <title>question - Student Helper Project</title>
        <meta property="og:title" content="question - Student Helper Project" />
      </Helmet>
      <UserHeader rootClassName="user-header-root-class-name3"></UserHeader>
      <div className="question-container1">
        <div className="question-container2">
          <div className="question-raiting">
            <button className="question-button button">
              <svg viewBox="0 0 1024 1024" className="question-icon">
                <path d="M170 512l342-342 342 342-62 60-238-238v520h-84v-520l-240 238z"></path>
              </svg>
            </button>
            <button className="question-button1 button">
              <svg viewBox="0 0 1024 1024" className="question-icon2">
                <path d="M854 512l-342 342-342-342 62-60 238 238v-520h84v520l240-238z"></path>
              </svg>
            </button>
            <span>+100500</span>
          </div>
          <div className="question-profile-info">
            <span>
              <span>Иван Иванов</span>
              <br></br>
              <span></span>
              <br></br>
              <span>Воронежский Государственный Университет</span>
              <br></br>
              <span></span>
              <br></br>
              <span>Рейтинг: 357</span>
            </span>
          </div>
        </div>
        <div className="question-question">
          <div className="question-container3">
            <span className="question-text11">Мат. анализ</span>
            <span className="question-text12">7:56 15.04.2022</span>
          </div>
          <h1>Помогите взять интеграл, пж</h1>
          <span className="question-text14">
            <span>
              Ребята, уже сил нет!!! Не могу взять интеграл! Пример интеграла во
              вложениях!!
            </span>
            <br></br>
            <span></span>
            <br></br>
            <span>
              Какой-то текст. Какой-то текст. Какой-то текст. Какой-то текст.
              Какой-то текст. Какой-то текст. Какой-то текст. Какой-то текст.
              Какой-то текст. Какой-то текст. Какой-то текст. Какой-то текст.
              Какой-то текст. Какой-то текст.
              <span
                dangerouslySetInnerHTML={{
                  __html: ' ',
                }}
              />
            </span>
          </span>
          <div className="question-files">
            <div className="question-container4">
              <svg viewBox="0 0 1024 1024" className="question-icon4">
                <path d="M554 384h236l-236-234v234zM256 86h342l256 256v512q0 34-26 59t-60 25h-512q-34 0-60-25t-26-59l2-684q0-34 25-59t59-25z"></path>
              </svg>
              <a
                href="https://example.com"
                target="_blank"
                rel="noreferrer noopener"
              >
                <span> file.jpg</span>
              </a>
            </div>
          </div>
          <div className="question-leave-comment">
            <textarea
              placeholder="Пиши свой ответ здесь!"
              className="question-textarea textarea"
            ></textarea>
            <label className="formLable">Прикрепить файл</label>
            <input
              type="file"
              placeholder="placeholder"
              className="question-textinput input"
            />
            <button className="question-button2 button">Оставить ответ</button>
          </div>
        </div>
      </div>
      <div className="question-answers">
        <h1>Ответы</h1>
        <AnswerCard></AnswerCard>
        <AnswerCard></AnswerCard>
        <AnswerCard></AnswerCard>
        <AnswerCard></AnswerCard>
      </div>
      <Footer rootClassName="footer-root-class-name6"></Footer>
    </div>
  )
}

export default Question
