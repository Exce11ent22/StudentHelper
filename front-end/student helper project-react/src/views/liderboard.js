import React from 'react'

import { Helmet } from 'react-helmet'

import UserHeader from '../components/user-header'
import LiderboardCard from '../components/liderboard-card'
import Footer from '../components/footer'
import './liderboard.css'

const Liderboard = (props) => {
  return (
    <div className="liderboard-container">
      <Helmet>
        <title>liderboard - Student Helper Project</title>
        <meta
          property="og:title"
          content="liderboard - Student Helper Project"
        />
      </Helmet>
      <UserHeader rootClassName="user-header-root-class-name2"></UserHeader>
      <div className="liderboard-liderboard">
        <h1 className="liderboard-text">
          <span>ТОП 10 ЭТОГО МЕСЯЦА</span>
        </h1>
        <LiderboardCard></LiderboardCard>
        <LiderboardCard></LiderboardCard>
        <LiderboardCard></LiderboardCard>
        <LiderboardCard></LiderboardCard>
        <LiderboardCard></LiderboardCard>
        <LiderboardCard></LiderboardCard>
      </div>
      <Footer rootClassName="footer-root-class-name5"></Footer>
    </div>
  )
}

export default Liderboard
