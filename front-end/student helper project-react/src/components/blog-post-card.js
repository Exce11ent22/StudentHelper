import React from 'react'
import { Link } from 'react-router-dom'

import PropTypes from 'prop-types'

import './blog-post-card.css'

const BlogPostCard = (props) => {
  return (
    <Link to="/question">
      <div className="blog-post-card-blog-post-card">
        <div className="blog-post-card-raiting">
          <svg viewBox="0 0 1024 1024" className="blog-post-card-icon">
            <path d="M170 512l342-342 342 342-62 60-238-238v520h-84v-520l-240 238z"></path>
          </svg>
          <svg viewBox="0 0 1024 1024" className="blog-post-card-icon2">
            <path d="M854 512l-342 342-342-342 62-60 238 238v-520h84v520l240-238z"></path>
          </svg>
          <span>{props.text}</span>
        </div>
        <div className="blog-post-card-container">
          <div className="blog-post-card-container1">
            <span className="blog-post-card-text1">{props.text1}</span>
            <span className="blog-post-card-text2">{props.text2}</span>
            <button className="blog-post-card-button button">
              {props.button}
            </button>
          </div>
          <h1 className="blog-post-card-text3">{props.heading}</h1>
        </div>
      </div>
    </Link>
  )
}

BlogPostCard.defaultProps = {
  button: 'Удалить',
  heading: 'Помогите взять интеграл, пж',
  text2: '23.04.2022',
  text1: 'Мат. анализ',
  text: '+100500',
}

BlogPostCard.propTypes = {
  button: PropTypes.string,
  heading: PropTypes.string,
  text2: PropTypes.string,
  text1: PropTypes.string,
  text: PropTypes.string,
}

export default BlogPostCard
