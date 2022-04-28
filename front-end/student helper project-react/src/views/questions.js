import React from 'react'

import { Helmet } from 'react-helmet'

import UserHeader from '../components/user-header'
import QuestionCard from '../components/question-card'
import Footer from '../components/footer'
import './questions.css'

const Questions = (props) => {
  return (
    <div className="questions-container">
      <Helmet>
        <title>questions - Student Helper Project</title>
        <meta
          property="og:title"
          content="questions - Student Helper Project"
        />
      </Helmet>
      <UserHeader></UserHeader>
      <div className="questions-questions">
        <div className="questions-search">
          <input
            type="text"
            placeholder="Поиск"
            className="questions-textinput input"
          />
          <button className="questions-button button">
            <svg
              viewBox="0 0 950.8571428571428 1024"
              className="questions-icon"
            >
              <path d="M658.286 475.429c0-141.143-114.857-256-256-256s-256 114.857-256 256 114.857 256 256 256 256-114.857 256-256zM950.857 950.857c0 40-33.143 73.143-73.143 73.143-19.429 0-38.286-8-51.429-21.714l-196-195.429c-66.857 46.286-146.857 70.857-228 70.857-222.286 0-402.286-180-402.286-402.286s180-402.286 402.286-402.286 402.286 180 402.286 402.286c0 81.143-24.571 161.143-70.857 228l196 196c13.143 13.143 21.143 32 21.143 51.429z"></path>
            </svg>
          </button>
          <button className="questions-button1 button">Фильтры</button>
        </div>
        <QuestionCard rootClassName="question-card-root-class-name1"></QuestionCard>
        <QuestionCard rootClassName="question-card-root-class-name4"></QuestionCard>
        <QuestionCard rootClassName="question-card-root-class-name5"></QuestionCard>
        <QuestionCard rootClassName="question-card-root-class-name6"></QuestionCard>
      </div>
      <Footer rootClassName="footer-root-class-name2"></Footer>
    </div>
  )
}

export default Questions
