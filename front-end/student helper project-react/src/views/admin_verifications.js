import React from 'react'

import { Helmet } from 'react-helmet'

import AdminHeader from '../components/admin-header'
import VerificationCard from '../components/verification-card'
import Footer from '../components/footer'
import './admin_verifications.css'

const AdminVerifications = (props) => {
  return (
    <div className="admin-verifications-container">
      <Helmet>
        <title>admin_verifications - Student Helper Project</title>
        <meta
          property="og:title"
          content="admin_verifications - Student Helper Project"
        />
      </Helmet>
      <AdminHeader rootClassName="admin-header-root-class-name2"></AdminHeader>
      <div className="admin-verifications-verifications-list">
        <VerificationCard></VerificationCard>
        <VerificationCard></VerificationCard>
        <VerificationCard></VerificationCard>
        <VerificationCard></VerificationCard>
        <VerificationCard></VerificationCard>
        <div className="admin-verifications-container1">
          <div className="admin-verifications-container2">
            <button className="admin-verifications-button button">
              <svg viewBox="0 0 1024 1024" className="admin-verifications-icon">
                <path d="M658 708l-60 60-256-256 256-256 60 60-196 196z"></path>
              </svg>
              <span className="admin-verifications-text">
                Предыдущая страница
              </span>
            </button>
          </div>
          <button className="admin-verifications-button1 button">
            <span className="admin-verifications-text1">
              <span>Следующая страница</span>
            </span>
            <svg viewBox="0 0 1024 1024" className="admin-verifications-icon2">
              <path d="M366 708l196-196-196-196 60-60 256 256-256 256z"></path>
            </svg>
          </button>
        </div>
      </div>
      <Footer rootClassName="footer-root-class-name12"></Footer>
    </div>
  )
}

export default AdminVerifications
