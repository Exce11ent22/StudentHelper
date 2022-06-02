import React from 'react'

import { Helmet } from 'react-helmet'

import AdminHeader from '../components/admin-header'
import Footer from '../components/footer'
import './admin_verivication.css'

const AdminVerivication = (props) => {
  return (
    <div className="admin-verivication-container">
      <Helmet>
        <title>admin_verivication - Student Helper Project</title>
        <meta
          property="og:title"
          content="admin_verivication - Student Helper Project"
        />
      </Helmet>
      <AdminHeader rootClassName="admin-header-root-class-name5"></AdminHeader>
      <div className="admin-verivication-container1">
        <label className="admin-verivication-text formLable">
          Данные пользователя на верификацию
        </label>
        <span className="admin-verivication-text01">
          <span>Иванов Иван Иванович</span>
          <br></br>
          <span></span>
          <br></br>
          <span>Факультет Компьютерных Наук</span>
          <br></br>
          <span></span>
          <br></br>
          <span>Направление: Программная инженерия</span>
          <br></br>
          <span></span>
          <br></br>
          <span>Фото студенческого:</span>
        </span>
        <div className="admin-verivication-files">
          <div className="admin-verivication-container2">
            <svg viewBox="0 0 1024 1024" className="admin-verivication-icon">
              <path d="M554 384h236l-236-234v234zM256 86h342l256 256v512q0 34-26 59t-60 25h-512q-34 0-60-25t-26-59l2-684q0-34 25-59t59-25z"></path>
            </svg>
            <a
              href="https://example.com"
              target="_blank"
              rel="noreferrer noopener"
            >
              <span>studak.jpg</span>
            </a>
          </div>
        </div>
        <button className="admin-verivication-button button">
          Верифицировать
        </button>
        <button className="admin-verivication-button1 button">Отклонить</button>
      </div>
      <Footer rootClassName="footer-root-class-name15"></Footer>
    </div>
  )
}

export default AdminVerivication
