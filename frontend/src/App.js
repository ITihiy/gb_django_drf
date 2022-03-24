import React from "react";
import './App.css';
import DRFUserList from './components/DRFUserList'
import ProjectList from "./components/ProjectList";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import {BrowserRouter, Link, Route, Routes} from "react-router-dom";
import axios from "axios";
import TODOList from "./components/TODOList";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'drf_users': [],
      'drf_projects': [],
      'drf_todos': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/drf_users/')
      .then(response => {
        const users = response.data;
        this.setState({
          'drf_users': users.results
        })
      })
      .catch(error => console.log(error));
    axios.get('http://127.0.0.1:8000/api/drf_projects/')
      .then(response => {
        const projects = response.data;
        this.setState({
          'drf_projects': projects.results
        })
      })
      .catch(error => console.log(error));
    axios.get('http://127.0.0.1:8000/api/drf_todo_items/')
      .then(response => {
        const todos = response.data;
        this.setState({
          'drf_todos': todos.results
        })
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <Menu/>
        <hr/>
        <BrowserRouter>
          <nav>
            <li><Link to='/'>Users</Link></li>
            <li><Link to='/projects/'>Projects</Link></li>
            <li><Link to='/todo_items/'>TODO items</Link></li>
          </nav>
          <Routes>
            <Route exact path='/' element={<DRFUserList drf_users={this.state.drf_users}/>}/>
            <Route exact path='/projects/' element={<ProjectList drf_projects={this.state.drf_projects}/>}/>
            <Route exact path='/todo_items/' element={<TODOList drf_todos={this.state.drf_todos}/>}/>
          </Routes>
        </BrowserRouter>
        <hr/>
        <Footer/>
      </div>
    )
  }
}

export default App;
