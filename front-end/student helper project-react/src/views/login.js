import React from 'react'
import { Link } from 'react-router-dom'

import { Helmet } from 'react-helmet'

import LoginHeader from '../components/login-header'
import Footer from '../components/footer'
import './login.css'

const Login = (props) => {
  return (
    <div className="login-container">
      <Helmet>
        <title>login - Student Helper Project</title>
        <meta property="og:title" content="login - Student Helper Project" />
      </Helmet>
      <LoginHeader></LoginHeader>
      <form className="login-form">
        <div className="login-container1">
          <label className="formLable">Введите ваш e-mail:</label>
          <input
            type="email"
            required
            placeholder="ivan.ivanov@mail.ru"
            className="login-textinput input"
          />
          <label className="formLable">Пароль</label>
          <input
            type="password"
            required
            placeholder="password"
            className="login-textinput1 input"
          />
          <button className="login-button button">Войти</button>
          <div className="login-container2">
            <Link to="/registration" className="login-button1 button">
              <span>
                <span>Регистрация</span>
                <span></span>
              </span>
            </Link>
            <a
              href="https://example.com"
              target="_blank"
              rel="noreferrer noopener"
            >
              Забыл пароль?
            </a>
          </div>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name"></Footer>
    </div>
  )
}

export default Login
