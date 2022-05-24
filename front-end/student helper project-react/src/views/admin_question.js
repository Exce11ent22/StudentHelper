import React from 'react'

import { Helmet } from 'react-helmet'

import AdminHeader from '../components/admin-header'
import AdminAnswerCard from '../components/admin-answer-card'
import Footer from '../components/footer'
import './admin_question.css'

const AdminQuestion = (props) => {
  return (
    <div className="admin-question-container">
      <Helmet>
        <title>admin_question - Student Helper Project</title>
        <meta
          property="og:title"
          content="admin_question - Student Helper Project"
        />
      </Helmet>
      <AdminHeader rootClassName="admin-header-root-class-name3"></AdminHeader>
      <div className="admin-question-container1">
        <div className="admin-question-container2">
          <div className="admin-question-raiting">
            <button className="admin-question-button button">
              <svg viewBox="0 0 1024 1024" className="admin-question-icon">
                <path d="M170 512l342-342 342 342-62 60-238-238v520h-84v-520l-240 238z"></path>
              </svg>
            </button>
            <button className="admin-question-button1 button">
              <svg viewBox="0 0 1024 1024" className="admin-question-icon2">
                <path d="M854 512l-342 342-342-342 62-60 238 238v-520h84v520l240-238z"></path>
              </svg>
            </button>
            <span>+100500</span>
          </div>
          <div className="admin-question-profile-info">
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
        <div className="admin-question-question">
          <div className="admin-question-container3">
            <span className="admin-question-text11">Мат. анализ</span>
            <span className="admin-question-text12">7:56 15.04.2022</span>
          </div>
          <h1>Помогите взять интеграл, пж</h1>
          <span className="admin-question-text14">
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
          <div className="admin-question-files">
            <div className="admin-question-container4">
              <svg viewBox="0 0 1024 1024" className="admin-question-icon4">
                <path d="M554 384h236l-236-234v234zM256 86h342l256 256v512q0 34-26 59t-60 25h-512q-34 0-60-25t-26-59l2-684q0-34 25-59t59-25z"></path>
              </svg>
              <a
                href="https://example.com"
                target="_blank"
                rel="noreferrer noopener"
              >
                <span>file.jpg</span>
              </a>
            </div>
          </div>
        </div>
        <button className="admin-question-button2 button">Удалить</button>
      </div>
      <div className="admin-question-answers">
        <h1>Ответы</h1>
        <AdminAnswerCard></AdminAnswerCard>
        <AdminAnswerCard></AdminAnswerCard>
        <AdminAnswerCard></AdminAnswerCard>
        <AdminAnswerCard></AdminAnswerCard>
      </div>
      <Footer rootClassName="footer-root-class-name13"></Footer>
    </div>
  )
}

export default AdminQuestion
