import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import './style.css'
import Liderboard from './views/liderboard'
import Change from './views/change'
import Registration from './views/registration'
import Questions from './views/questions'
import AdminVerivication from './views/admin_verivication'
import Ask from './views/ask'
import Index from './views/index'
import AdminListOfAdministrators from './views/admin_list_of_administrators'
import LoginAdmin from './views/login_admin'
import AdminQuestions from './views/admin_questions'
import AdminQuestion from './views/admin_question'
import Question from './views/question'
import Verification from './views/verification'
import AdminVerifications from './views/admin_verifications'
import AdminChangeRole from './views/admin_change_role'
import Login from './views/login'
import Profile from './views/profile'
import AdminAssignRole from './views/admin_assign_role'

const App = () => {
  return (
    <Router>
      <div>
        <Route exact component={Liderboard} path="/liderboard" />
        <Route exact component={Change} path="/change" />
        <Route exact component={Registration} path="/registration" />
        <Route exact component={Questions} path="/questions" />
        <Route exact component={AdminVerivication} path="/admin_verivication" />
        <Route exact component={Ask} path="/ask" />
        <Route exact component={Index} path="/" />
        <Route
          exact
          component={AdminListOfAdministrators}
          path="/admin_list_of_administrators"
        />
        <Route exact component={LoginAdmin} path="/login_admin" />
        <Route exact component={AdminQuestions} path="/admin_questions" />
        <Route exact component={AdminQuestion} path="/admin_question" />
        <Route exact component={Question} path="/question" />
        <Route exact component={Verification} path="/verification" />
        <Route
          exact
          component={AdminVerifications}
          path="/admin_verifications"
        />
        <Route exact component={AdminChangeRole} path="/admin_change_role" />
        <Route exact component={Login} path="/login" />
        <Route exact component={Profile} path="/profile" />
        <Route exact component={AdminAssignRole} path="/admin_assign_role" />
      </div>
    </Router>
  )
}

ReactDOM.render(<App />, document.getElementById('app'))
