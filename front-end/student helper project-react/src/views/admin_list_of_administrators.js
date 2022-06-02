import React from 'react'

import { Helmet } from 'react-helmet'

import AdminHeader from '../components/admin-header'
import AdminCard from '../components/admin-card'
import Footer from '../components/footer'
import './admin_list_of_administrators.css'

const AdminListOfAdministrators = (props) => {
  return (
    <div className="admin-list-of-administrators-container">
      <Helmet>
        <title>admin_list_of_administrators - Student Helper Project</title>
        <meta
          property="og:title"
          content="admin_list_of_administrators - Student Helper Project"
        />
      </Helmet>
      <AdminHeader rootClassName="admin-header-root-class-name1"></AdminHeader>
      <div className="admin-list-of-administrators-list-of-administrators">
        <AdminCard></AdminCard>
        <AdminCard></AdminCard>
        <AdminCard></AdminCard>
        <AdminCard></AdminCard>
        <AdminCard></AdminCard>
        <div className="admin-list-of-administrators-container1">
          <div className="admin-list-of-administrators-container2">
            <button className="admin-list-of-administrators-button button">
              <svg
                viewBox="0 0 1024 1024"
                className="admin-list-of-administrators-icon"
              >
                <path d="M658 708l-60 60-256-256 256-256 60 60-196 196z"></path>
              </svg>
              <span className="admin-list-of-administrators-text">
                Предыдущая страница
              </span>
            </button>
          </div>
          <button className="admin-list-of-administrators-button1 button">
            <span className="admin-list-of-administrators-text1">
              <span>Следующая страница</span>
            </span>
            <svg
              viewBox="0 0 1024 1024"
              className="admin-list-of-administrators-icon2"
            >
              <path d="M366 708l196-196-196-196 60-60 256 256-256 256z"></path>
            </svg>
          </button>
        </div>
      </div>
      <Footer rootClassName="footer-root-class-name11"></Footer>
    </div>
  )
}

export default AdminListOfAdministrators
