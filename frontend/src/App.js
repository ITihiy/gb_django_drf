import React from "react";
import './App.css';
import DRFUserList from './components/DRFUserList'
import ProjectList from "./components/ProjectList";
import Menu from "./components/Menu";
import LoginForm from "./components/LoginForm";
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
      'drf_todos': [],
      'token': ''
    }
  }

  getData() {
    let headers = this.getHeader();

    axios.get('http://127.0.0.1:8000/api/drf_users/', {headers})
      .then(response => {
        const users = response.data;
        this.setState({
          'drf_users': users.results
        })
      })
      .catch(error => {
        console.log(error);
        this.setState({'drf_users': []})
      });
    axios.get('http://127.0.0.1:8000/api/drf_projects/', {headers})
      .then(response => {
        const projects = response.data;
        this.setState({
          'drf_projects': projects.results
        })
      })
      .catch(error => {
        console.log(error);
        this.setState({'drf_projects': []})
      });
    axios.get('http://127.0.0.1:8000/api/drf_todo_items/', {headers})
      .then(response => {
        const todos = response.data;
        this.setState({
          'drf_todos': todos.results
        })
      })
      .catch(
        error => {
          console.log(error);
          this.setState({'drf_todos': []});
        }
      )
  }

  componentDidMount() {
    let token = localStorage.getItem('token');
    this.setState({'token': token}, this.getData);
  }

  isAuth() {
    return !!this.state.token
  }

  getHeader() {
    if (this.isAuth()) {
      return {'Authorization': 'Token ' + this.state.token}
    }
    return {}
  }

  logout() {
    localStorage.setItem('token', '');
    this.setState({'token': ''}, this.getData)
  }

  getToken(login, password) {
    axios.post('http://127.0.0.1:8000/api-get-token/', {'username': login, 'password': password})
      .then(response => {
        const token = response.data.token;
        localStorage.setItem('token', token);
        console.log(response.data);
        this.setState({
          'token': token
        });
      }).then(() => {
        this.getData()
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
            <li>
              {this.isAuth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login/'>Login</Link>}
            </li>
          </nav>
          <Routes>
            <Route exact path='/' element={<DRFUserList drf_users={this.state.drf_users}/>}/>
            <Route exact path='/projects/' element={<ProjectList drf_projects={this.state.drf_projects}/>}/>
            <Route exact path='/login/'
                   element={<LoginForm getToken={(login, password) => this.getToken(login, password)}/>}/>
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
