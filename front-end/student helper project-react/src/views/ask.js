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
            required
            placeholder="ivan.ivanov@mail.ru"
            className="ask-textinput1 input"
          />
          <div className="ask-container2">
            <select className="ask-select">
              <option value="Option 1" selected>
                Мат. анализ
              </option>
              <option value="Option 2">Теория вероятностей</option>
              <option value="Option 3">Линейная алгебра</option>
            </select>
            <button className="ask-button button">Публиковать</button>
          </div>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name3"></Footer>
    </div>
  )
}

export default Ask
