import React from 'react'
import { Link } from 'react-router-dom'

import { Helmet } from 'react-helmet'

import IndexHeader from '../components/index-header'
import Footer from '../components/footer'
import './index.css'

const Index = (props) => {
  return (
    <div className="index-container">
      <Helmet>
        <title>Student Helper Project</title>
        <meta property="og:title" content="Student Helper Project" />
      </Helmet>
      <IndexHeader></IndexHeader>
      <div className="index-hero">
        <div className="index-container1">
          <h1 className="index-text">Просто сказка!</h1>
          <span className="index-text1">
            <span>
              <span>
                Student Helper - это форум для взаимопомощи студентов. Здесь ты
                можешь как помочь кому-нибудь, так и сам задать вопрос, который
                не дает спать (потому что готовишься к сессии, хи-хи). Если ты
                будешь активным и полезным участником, то можешь рассчитывать на
                небольшое пожертвование!
              </span>
            </span>
            <span></span>
            <span></span>
          </span>
          <div className="index-btn-group">
            <Link to="/questions" className="index-navlink button">
              Начнем!
            </Link>
            <Link to="/ask" className="index-navlink1 button">
              Задать вопрос
            </Link>
          </div>
        </div>
        <img
          alt="image"
          src="https://images.unsplash.com/photo-1525498128493-380d1990a112?ixid=Mnw5MTMyMXwwfDF8c2VhcmNofDI0fHxtaW5pbWFsaXNtJTIwZ3JlZW58ZW58MHx8fHwxNjI1ODQxMDcw&amp;ixlib=rb-1.2.1&amp;h=1200"
          className="index-image"
        />
      </div>
      <Footer></Footer>
    </div>
  )
}

export default Index
