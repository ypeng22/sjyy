import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import backend from './backend';

// Year, languages, skills, focus area, time zone, project idea, hackathon experience, major, about me section.


class HackerProfile extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      fname: props.fname,
      lname: props.lname,
      year: props.year,
      langs: props.langs,
      skills: props.skills,
      fa: props.fa,
      zone: props.zone,
      idea: props.idea,
      exp: props.exp,
      major: props.major,
      bio: props.bio,
    };
  }

  render(){
    return(
      <div className="hacker">
        <div className="name">{this.state.fname +' '+ this.state.lname}</div>
          <ul className="prof">
            <li className="pfield"><b>Year: </b>{this.state.year}</li>
            <li className="pfield"><b>Languages: </b>{this.state.langs}</li>
            <li className="pfield"><b>Skills: </b>{this.state.skills}</li>
            <li className="pfield"><b>Area of Focus: </b>{this.state.fa}</li>
            <li className="pfield"><b>Timezone: </b>{this.state.zone}</li>
            <li className="pfield"><b>Project Idea: </b>{this.state.idea}</li>
            <li className="pfield"><b>Previous Hackathons: </b>{this.state.exp}</li>
            <li className="pfield"><b>Major: </b>{this.state.major}</li>
            <li className="pfield"><b>About: </b>{this.state.bio}</li>
          </ul>
      </div>
    );
  }
}



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

    var pf1 = {
      fname: "Rob",
      lname: "Boss",
      year: 4,
      langs: "Java, HTML, CSS, Python",
      skills: "Android APIs and COM project architecture",
      fa: "Mobile Web App Development",
      zone: "CEST",
      idea: "Candy Crush 2: Electric Boogaloo",
      exp: 3,
      major: "Computer Science",
      bio: "lets make a code together!",
    };
    const pf2 = {
      fname: "Rodly",
      lname: "Swiplen",
      year: 1,
      langs: "x86 Intel Assembly, FORTRAN, LISP",
      skills: "reverse engineering and manual analysis of runtime memory",
      fa: "Console Hardware Emulation",
      zone: "CET",
      idea: "N64 Emulation software that runs on my WiiU hardware emulator",
      exp: 0,
      major: "Computer Science",
      bio: "optimize first, ask questions later.",
    };
    
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
            <HackerProfile 
              fname={pf1.fname}
              lname={pf1.lname}
              year={pf1.year}
              langs={pf1.langs}
              skills={pf1.skills}
              fa={pf1.fa}
              zone={pf1.zone}
              idea={pf1.idea}
              exp={pf1.exp}
              major={pf1.major}
              bio={pf1.bio}/>
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