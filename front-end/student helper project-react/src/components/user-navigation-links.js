import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './user-navigation-links.css'

const UserNavigationLinks = (props) => {
  return (
    <nav className={`user-navigation-links-nav ${props.rootClassName} `}>
      <Link to="/questions" className="user-navigation-links-navlink">
        {props.text}
      </Link>
      <Link to="/ask" className="user-navigation-links-navlink1">
        {props.text1}
      </Link>
      <Link to="/profile" className="user-navigation-links-navlink2">
        {props.text2}
      </Link>
      <Link to="/liderboard" className="user-navigation-links-navlink3">
        {props.text3}
      </Link>
    </nav>
  )
}

UserNavigationLinks.defaultProps = {
  rootClassName: '',
  text1: 'Задать вопрос',
  text3: 'Таблица лидеров',
  text: 'Вопросы',
  text2: 'Профиль',
}

UserNavigationLinks.propTypes = {
  rootClassName: PropTypes.string,
  text1: PropTypes.string,
  text3: PropTypes.string,
  text: PropTypes.string,
  text2: PropTypes.string,
}

export default UserNavigationLinks
