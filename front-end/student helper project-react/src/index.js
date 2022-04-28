import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import './style.css'
import Liderboard from './views/liderboard'
import Change from './views/change'
import Registration from './views/registration'
import Questions from './views/questions'
import Ask from './views/ask'
import Index from './views/index'
import Question from './views/question'
import Verification from './views/verification'
import Login from './views/login'
import Profile from './views/profile'

const App = () => {
  return (
    <Router>
      <div>
        <Route exact component={Liderboard} path="/liderboard" />
        <Route exact component={Change} path="/change" />
        <Route exact component={Registration} path="/registration" />
        <Route exact component={Questions} path="/questions" />
        <Route exact component={Ask} path="/ask" />
        <Route exact component={Index} path="/" />
        <Route exact component={Question} path="/question" />
        <Route exact component={Verification} path="/verification" />
        <Route exact component={Login} path="/login" />
        <Route exact component={Profile} path="/profile" />
      </div>
    </Router>
  )
}

ReactDOM.render(<App />, document.getElementById('app'))
