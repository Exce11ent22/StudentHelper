import React from 'react'

import { Helmet } from 'react-helmet'

import IndexHeader from '../components/index-header'
import Footer from '../components/footer'
import './verification.css'

const Verification = (props) => {
  return (
    <div className="verification-container">
      <Helmet>
        <title>verification - Student Helper Project</title>
        <meta
          property="og:title"
          content="verification - Student Helper Project"
        />
      </Helmet>
      <IndexHeader rootClassName="index-header-root-class-name"></IndexHeader>
      <form className="verification-form">
        <div className="verification-container1">
          <label className="formLable">Ваш факультет:</label>
          <input
            type="text"
            required
            placeholder="Факультет компьютерных наук"
            className="verification-textinput input"
          />
          <label className="formLable">Ваша специальность</label>
          <input
            type="text"
            required
            placeholder="Программная инженерия"
            className="verification-textinput1 input"
          />
          <label className="formLable">
            Загрузить фото студенческого [ jpg]
          </label>
          <input
            type="file"
            required
            placeholder="ivan.ivanov@mail.ru"
            className="verification-textinput2 input"
          />
          <button className="verification-button button">
            Отправить данные на верификацию
          </button>
        </div>
      </form>
      <Footer rootClassName="footer-root-class-name8"></Footer>
    </div>
  )
}

export default Verification
