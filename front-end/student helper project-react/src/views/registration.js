import React from 'react'

import { Helmet } from 'react-helmet'

import LoginHeader from '../components/login-header'
import Footer from '../components/footer'
import './registration.css'

const Registration = (props) => {
  return (
    <div className="registration-container">
      <Helmet>
        <title>registration - Student Helper Project</title>
        <meta
          property="og:title"
          content="registration - Student Helper Project"
        />
      </Helmet>
      <LoginHeader rootClassName="login-header-root-class-name"></LoginHeader>
      <form className="registration-form">
        <div className="registration-h-container1">
          <div className="registration-v-container1">
            <label className="formLable">Имя</label>
            <input
              type="text"
              required
              placeholder="Иван"
              className="registration-textinput input"
            />
            <label className="formLable">Фамилия</label>
            <input
              type="text"
              required
              placeholder="Иванов"
              className="registration-textinput1 input"
            />
            <label className="formLable">Пароль</label>
            <input
              type="password"
              required
              placeholder="password"
              className="registration-textinput2 input"
            />
            <label className="formLable">Подтверждение пароля</label>
            <input
              type="password"
              required
              placeholder="password (confirm)"
              className="registration-textinput3 input"
            />
          </div>
          <div className="registration-v-container2">
            <label className="formLable">Почта</label>
            <input
              type="email"
              required
              placeholder="ivan.ivanov@mail.ru"
              className="registration-textinput4 input"
            />
            <label className="formLable">Учебное заведение</label>
            <input
              type="text"
              required
              placeholder="Полное название заведения"
              className="registration-textinput5 input"
            />
            <label className="formLable">Дата поступления</label>
            <input
              type="date"
              required
              placeholder="2000-01-01"
              className="registration-textinput6 input"
            />
            <button className="registration-button button">
              <span>
                <span>Регистрация</span>
                <span></span>
              </span>
            </button>
          </div>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name1"></Footer>
    </div>
  )
}

export default Registration
