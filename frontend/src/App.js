import React from "react";
import './App.css';
import DRFUserList from './components/DRFUserList'
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import axios from "axios";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'drf_users': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/drf_users/')
      .then(response => {
        const users = response.data;
        this.setState({
          'drf_users': users
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
        <hr/>
        <Footer/>
      </div>
    )
  }
}

export default App;
