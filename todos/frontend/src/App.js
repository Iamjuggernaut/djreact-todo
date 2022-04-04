import React from 'react'
import './App.css';
import UserList from './components/Users';
import axios from 'axios'
import Navbar from './components/Navbar';
import Footer from './components/Footer';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        const users = response.data
        this.setState(
          { 'users': users }
        )
      }).catch(error => console.log(error))
  }


  render() {
    return (
      <div className='App'>
        <Navbar />
        <UserList users={this.state.users} />
        <Footer />
      </div>
    )
  }
}

export default App;
