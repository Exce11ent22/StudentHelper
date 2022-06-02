import React from 'react'

import { Helmet } from 'react-helmet'

import LoginHeader from '../components/login-header'
import Footer from '../components/footer'
import './login_admin.css'

const LoginAdmin = (props) => {
  return (
    <div className="login-admin-container">
      <Helmet>
        <title>login_admin - Student Helper Project</title>
        <meta
          property="og:title"
          content="login_admin - Student Helper Project"
        />
      </Helmet>
      <LoginHeader></LoginHeader>
      <form className="login-admin-form">
        <div className="login-admin-container1">
          <label className="formLable">Введите ваш e-mail:</label>
          <input
            type="email"
            required
            placeholder="ivan.ivanov@mail.ru"
            className="login-admin-textinput input"
          />
          <label className="formLable">Пароль</label>
          <input
            type="password"
            required
            placeholder="password"
            className="login-admin-textinput1 input"
          />
          <button className="login-admin-button button">Войти</button>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name16"></Footer>
    </div>
  )
}

export default LoginAdmin
