import React from 'react'

import { Helmet } from 'react-helmet'

import AdminHeader from '../components/admin-header'
import Footer from '../components/footer'
import './admin_assign_role.css'

const AdminAssignRole = (props) => {
  return (
    <div className="admin-assign-role-container">
      <Helmet>
        <title>admin_assign_role - Student Helper Project</title>
        <meta
          property="og:title"
          content="admin_assign_role - Student Helper Project"
        />
      </Helmet>
      <AdminHeader rootClassName="admin-header-root-class-name"></AdminHeader>
      <form className="admin-assign-role-form">
        <label className="formLable">e-mail</label>
        <input
          type="email"
          required
          placeholder="ivanivanov@mail.ru"
          className="admin-assign-role-textinput input"
        />
        <label className="formLable">Выберите роль</label>
        <select required className="admin-assign-role-select">
          <option value="administrator" selected>
            Администратор
          </option>
          <option value="moderator">Модератор</option>
        </select>
        <button className="admin-assign-role-button button">
          Назначить роль
        </button>
      </form>
      <Footer rootClassName="footer-root-class-name10"></Footer>
    </div>
  )
}

export default AdminAssignRole
