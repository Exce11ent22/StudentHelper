import React from 'react'
import { Link } from 'react-router-dom'

import { Helmet } from 'react-helmet'

import UserHeader from '../components/user-header'
import Footer from '../components/footer'
import './profile.css'

const Profile = (props) => {
  return (
    <div className="profile-container">
      <Helmet>
        <title>profile - Student Helper Project</title>
        <meta property="og:title" content="profile - Student Helper Project" />
      </Helmet>
      <UserHeader rootClassName="user-header-root-class-name1"></UserHeader>
      <div className="profile-hero">
        <img
          alt="image"
          src="https://images.unsplash.com/photo-1529859503572-5b9d1e68e952?ixid=Mnw5MTMyMXwwfDF8c2VhcmNofDN8fG1pbmltYWxpc20lMjBjb3VjaHxlbnwwfHx8fDE2MjYxODI1OTE&amp;ixlib=rb-1.2.1&amp;w=1200"
          className="profile-image"
        />
        <div className="profile-container1">
          <h1 className="profile-text">Иван Иванов</h1>
          <h2 className="profile-text01">Верифицирован</h2>
          <div className="profile-btn-group">
            <Link to="/change" className="profile-navlink button">
              Редактировать данные
            </Link>
            <Link to="/verification" className="profile-navlink1 button">
              Верификация
            </Link>
          </div>
          <span>
            <span>Почта: ivan.ivanov@mail.ru</span>
            <br></br>
            <span></span>
            <br></br>
            <span>
              Учебное заведение: Воронежский Государственный Университет
            </span>
            <br></br>
            <span></span>
            <br></br>
            <span>Факультет: Факультет компьютерных наук</span>
            <br></br>
            <span></span>
            <br></br>
            <span>Специальность: Программная Инженерия</span>
            <br></br>
            <span></span>
            <br></br>
            <span>Рейтинг: 357f</span>
          </span>
        </div>
      </div>
      <Footer rootClassName="footer-root-class-name4"></Footer>
    </div>
  )
}

export default Profile
