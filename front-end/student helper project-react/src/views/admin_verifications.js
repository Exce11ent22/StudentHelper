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
      </div>
      <Footer rootClassName="footer-root-class-name12"></Footer>
    </div>
  )
}

export default AdminVerifications
