import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import backend from './backend';

class ShortEntry extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      id: props.id,
      label: props.label,
      placeholder: props.placeholder,
      updateFn: props.updateFn,
    };
  }

  UpdateCallback = (event) => {
    this.setState({value: event.target.value});
  }
  render(){
    return(
      <div className="row">
        <div className="col-25">
          <label for={this.state.id}>{this.state.label}</label>
          <input 
          type="text" 
            id={this.state.id} 
            name={this.state.id} 
            placeholder={this.state.placeholder} 
            onChange={this.state.updateFn}/>
        </div>
      </div>
    );
  }
}
class LongEntry extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: props.id,
      label: props.label,
      placeholder: props.placeholder,
      updateFn: props.updateFn,
    };
  }

  render() {
    return (
      <div className="row">
        <div className="col-25">
          <label for={this.state.id}>{this.state.label}</label>
        </div>
        <div className="col-75">
          <textarea
            id={this.state.id}
            name={this.state.id}
            placeholder={this.state.placeholder}
            onChange={this.state.updateFn} 
            style={{ height: '200px' }} />
        </div>
      </div>
    );
  }
}

class DropdownSelection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: props.id,
      label: props.label,
      selections: props.selections,
      updateFn: props.updateFn,
    };
  }

  render() {
    let options;
    options = this.state.selections.map((selection) => {
      return(
        <option value={selection}>
          {selection}
        </option>
      );
    })

    return (
      <div className="row">
        <div className="col-25">
          <label for={this.state.id}>{this.state.label}</label>
          <select
            id={this.state.id}
            name={this.state.id}
            onChange={this.state.updateFn}>
              {options}
          </select>
        </div>
      </div>
    );
  }
}

class Signup extends React.Component {
  MatchType = ['a new team', 'team members'];
  constructor(props){
    super(props);
    this.state = {
      firstname: null,
      lastname: null,
      match_t: null,
      bio: null,
    };
  }

  SubmitCallback = () =>{
    backend.addUser(this.state.firstname + " " + this.state.lastname, this.state.match_t, this.state.bio);
  }

  UpdateFirstName = (event) => {
    this.setState({ firstname: event.target.value });
  }
  UpdateLastName = (event) => {
    this.setState({ lastname: event.target.value });
  }
  UpdateMatchType = (event) => {
    this.setState({ match_t: event.target.value });
  }
  UpdateBio = (event) => {
    this.setState({ bio: event.target.value });
  }



  render() {
    
    return (
      <div className="container">
        <form onSubmit={this.SubmitCallback}>
          <ShortEntry
            id="fname"
            label='First Name:'
            placeholder="Enter your first name"
            updateFn={this.UpdateFirstName}
          />
          <ShortEntry
            id="lname"
            label='Last Name:'
            placeholder="Enter your last name"
            updateFn={this.UpdateLastName}
          />
          <DropdownSelection
            id="match_t"
            label="Looking for: "
            selections={this.MatchType}
            updateFn={this.UpdateMatchType}
            />
          <LongEntry
            id="bio"
            label='Bio:'
            placeholder="Talk about yourself!"
            updateFn={this.UpdateBio}
            />
              <div className="row">
                <input type="submit" value="Submit"/>
          </div>
        </form>
      </div>
    );
  }
}


ReactDOM.render(
  <Signup />,
  document.getElementById('root')
);