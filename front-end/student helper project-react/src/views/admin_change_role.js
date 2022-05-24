import React from 'react'

import { Helmet } from 'react-helmet'

import AdminHeader from '../components/admin-header'
import Footer from '../components/footer'
import './admin_change_role.css'

const AdminChangeRole = (props) => {
  return (
    <div className="admin-change-role-container">
      <Helmet>
        <title>admin_change_role - Student Helper Project</title>
        <meta
          property="og:title"
          content="admin_change_role - Student Helper Project"
        />
      </Helmet>
      <AdminHeader rootClassName="admin-header-root-class-name4"></AdminHeader>
      <form className="admin-change-role-form">
        <label className="formLable">Имя</label>
        <input
          type="text"
          placeholder="Иван"
          required
          className="admin-change-role-input input"
        />
        <label className="formLable">Фамилия</label>
        <input
          type="text"
          placeholder="Иванов"
          className="admin-change-role-textinput input"
        />
        <label className="formLable">e-mail</label>
        <input
          type="email"
          placeholder="ivanivanov@mail.ru"
          required
          className="admin-change-role-textinput1 input"
        />
        <label className="formLable">Специальный пароль</label>
        <input
          type="password"
          placeholder="пароль"
          required
          className="admin-change-role-textinput2 input"
        />
        <label className="formLable">Выберите роль</label>
        <select required className="admin-change-role-select">
          <option value="administrator" selected>
            Администратор
          </option>
          <option value="moderator">Модератор</option>
        </select>
        <button className="admin-change-role-button button">Изменить</button>
      </form>
      <Footer rootClassName="footer-root-class-name14"></Footer>
    </div>
  )
}

export default AdminChangeRole
