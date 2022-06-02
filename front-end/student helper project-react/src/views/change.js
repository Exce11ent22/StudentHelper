import React from 'react'

import { Helmet } from 'react-helmet'

import UserHeader from '../components/user-header'
import Footer from '../components/footer'
import './change.css'

const Change = (props) => {
  return (
    <div className="change-container">
      <Helmet>
        <title>change - Student Helper Project</title>
        <meta property="og:title" content="change - Student Helper Project" />
      </Helmet>
      <UserHeader rootClassName="user-header-root-class-name4"></UserHeader>
      <form className="change-form">
        <div className="change-container1">
          <div className="change-h-container1">
            <div className="change-v-container1">
              <label className="formLable">Имя</label>
              <input
                type="text"
                required
                placeholder="Иван"
                className="change-textinput input"
              />
              <label className="formLable">Фамилия</label>
              <input
                type="text"
                required
                placeholder="Иванов"
                className="change-textinput1 input"
              />
              <label className="formLable">Пароль</label>
              <input
                type="password"
                required
                placeholder="password"
                className="change-textinput2 input"
              />
            </div>
            <div className="change-v-container2">
              <label className="formLable">Почта</label>
              <input
                type="email"
                required
                placeholder="ivan.ivanov@mail.ru"
                className="change-textinput3 input"
              />
              <label className="formLable">Учебное заведение</label>
              <input
                type="text"
                required
                placeholder="Полное название заведения"
                className="change-textinput4 input"
              />
              <label className="formLable">Дата поступления</label>
              <input
                type="date"
                required
                placeholder="2000-01-01"
                className="change-textinput5 input"
              />
            </div>
          </div>
          <button className="change-button button">
            <span>
              <span>Изменить данные</span>
            </span>
          </button>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name7"></Footer>
    </div>
  )
}

export default Change
