import React from 'react'

import { Helmet } from 'react-helmet'

import UserHeader from '../components/user-header'
import Footer from '../components/footer'
import './ask.css'

const Ask = (props) => {
  return (
    <div className="ask-container">
      <Helmet>
        <title>ask - Student Helper Project</title>
        <meta property="og:title" content="ask - Student Helper Project" />
      </Helmet>
      <UserHeader rootClassName="user-header-root-class-name"></UserHeader>
      <form className="ask-form">
        <div className="ask-container1">
          <label className="formLable">Заголовок вопроса</label>
          <input
            type="text"
            required
            placeholder="Помогите взять интеграл, пж"
            className="ask-textinput input"
          />
          <label className="formLable">Описание вопроса</label>
          <textarea
            placeholder="Не могу взять интеграл, помогите!!! Прикрепил пример интеграла во вложениях!"
            className="ask-textarea textarea"
          ></textarea>
          <div className="ask-files">
            <div className="ask-container2">
              <svg viewBox="0 0 1024 1024" className="ask-icon">
                <path d="M554 384h236l-236-234v234zM256 86h342l256 256v512q0 34-26 59t-60 25h-512q-34 0-60-25t-26-59l2-684q0-34 25-59t59-25z"></path>
              </svg>
              <a
                href="https://example.com"
                target="_blank"
                rel="noreferrer noopener"
              >
                https://studenthelper/file/1346134613
              </a>
            </div>
            <div className="ask-container3">
              <svg viewBox="0 0 1024 1024" className="ask-icon2">
                <path d="M554 384h236l-236-234v234zM256 86h342l256 256v512q0 34-26 59t-60 25h-512q-34 0-60-25t-26-59l2-684q0-34 25-59t59-25z"></path>
              </svg>
              <a
                href="https://example.com"
                target="_blank"
                rel="noreferrer noopener"
              >
                https://studenthelper/file/309486098
              </a>
            </div>
          </div>
          <div className="ask-container4">
            <select>
              <option value="Option 1" selected>
                Мат. анализ
              </option>
              <option value="Option 2">Теория вероятностей</option>
              <option value="Option 3">Линейная алгебра</option>
            </select>
            <button className="button">Прикрепить файл</button>
            <button className="ask-button1 button">Публиковать</button>
          </div>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name3"></Footer>
    </div>
  )
}

export default Ask
