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
      </div>
      <Footer rootClassName="footer-root-class-name11"></Footer>
    </div>
  )
}

export default AdminListOfAdministrators
