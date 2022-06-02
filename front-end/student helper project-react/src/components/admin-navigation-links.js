import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './admin-navigation-links.css'

const AdminNavigationLinks = (props) => {
  return (
    <nav className="admin-navigation-links-admin-navigation-links">
      <Link to="/admin_questions" className="admin-navigation-links-navlink">
        {props.text}
      </Link>
      <Link to="/admin_assign_role" className="admin-navigation-links-navlink1">
        {props.text1}
      </Link>
      <Link
        to="/admin_list_of_administrators"
        className="admin-navigation-links-navlink2"
      >
        {props.text2}
      </Link>
      <Link
        to="/admin_verifications"
        className="admin-navigation-links-navlink3"
      >
        {props.text3}
      </Link>
    </nav>
  )
}

AdminNavigationLinks.defaultProps = {
  text: 'Вопросы',
  text2: 'Список модераторов',
  text3: 'Заявки на верификацию',
  text1: 'Назначить роль',
}

AdminNavigationLinks.propTypes = {
  text: PropTypes.string,
  text2: PropTypes.string,
  text3: PropTypes.string,
  text1: PropTypes.string,
}

export default AdminNavigationLinks
