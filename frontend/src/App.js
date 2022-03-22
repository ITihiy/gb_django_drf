import React from "react";
import './App.css';
import DRFUserList from './components/DRFUserList'
import ProjectList from "./components/ProjectList";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import axios from "axios";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'drf_users': [],
      'drf_projects': []
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
      .catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/drf_projects/')
      .then(response => {
        const projects = response.data;
        this.setState({
          'drf_projects': projects.results
        })
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <Menu/>
        <hr/>
        <DRFUserList drf_users={this.state.drf_users}/>
        <ProjectList drf_projects={this.state.drf_projects}/>
        <hr/>
        <Footer/>
      </div>
    )
  }
}

export default App;
