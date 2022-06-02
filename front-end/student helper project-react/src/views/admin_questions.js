import React from 'react'

import { Helmet } from 'react-helmet'

import AdminHeader from '../components/admin-header'
import QuestionCardAdmin from '../components/question-card-admin'
import Footer from '../components/footer'
import './admin_questions.css'

const AdminQuestions = (props) => {
  return (
    <div className="admin-questions-container">
      <Helmet>
        <title>admin_questions - Student Helper Project</title>
        <meta
          property="og:title"
          content="admin_questions - Student Helper Project"
        />
      </Helmet>
      <AdminHeader></AdminHeader>
      <div className="admin-questions-questions">
        <div className="admin-questions-search">
          <input
            type="text"
            placeholder="Поиск"
            className="admin-questions-textinput input"
          />
          <button className="admin-questions-button button">
            <svg
              viewBox="0 0 950.8571428571428 1024"
              className="admin-questions-icon"
            >
              <path d="M658.286 475.429c0-141.143-114.857-256-256-256s-256 114.857-256 256 114.857 256 256 256 256-114.857 256-256zM950.857 950.857c0 40-33.143 73.143-73.143 73.143-19.429 0-38.286-8-51.429-21.714l-196-195.429c-66.857 46.286-146.857 70.857-228 70.857-222.286 0-402.286-180-402.286-402.286s180-402.286 402.286-402.286 402.286 180 402.286 402.286c0 81.143-24.571 161.143-70.857 228l196 196c13.143 13.143 21.143 32 21.143 51.429z"></path>
            </svg>
          </button>
          <button className="admin-questions-button1 button">Фильтры</button>
        </div>
        <QuestionCardAdmin></QuestionCardAdmin>
        <QuestionCardAdmin></QuestionCardAdmin>
        <QuestionCardAdmin></QuestionCardAdmin>
        <QuestionCardAdmin></QuestionCardAdmin>
        <div className="admin-questions-container1">
          <div className="admin-questions-container2">
            <button className="admin-questions-button2 button">
              <svg viewBox="0 0 1024 1024" className="admin-questions-icon2">
                <path d="M658 708l-60 60-256-256 256-256 60 60-196 196z"></path>
              </svg>
              <span className="admin-questions-text">Предыдущая страница</span>
            </button>
          </div>
          <button className="admin-questions-button3 button">
            <span className="admin-questions-text1">
              <span>Следующая страница</span>
            </span>
            <svg viewBox="0 0 1024 1024" className="admin-questions-icon4">
              <path d="M366 708l196-196-196-196 60-60 256 256-256 256z"></path>
            </svg>
          </button>
        </div>
      </div>
      <Footer rootClassName="footer-root-class-name9"></Footer>
    </div>
  )
}

export default AdminQuestions
