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
          <label className="formLable">Прикрепить файл</label>
          <input
            type="file"
            placeholder="ivan.ivanov@mail.ru"
            className="ask-textinput1 input"
          />
          <div className="ask-container2">
            <input
              type="text"
              required
              placeholder="Какой предмет?"
              className="ask-textinput2 input"
            />
            <button className="ask-button button">Публиковать</button>
          </div>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name3"></Footer>
    </div>
  )
}

export default Ask
