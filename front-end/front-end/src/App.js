import "./App.css";
import Navbar from "./Navbar";
import Home from "./Home";
import InjuryList from "./InjuryList";
import axios from "axios";
import React, { Component } from "react";


function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="content">
        <Home />
      </div>
    </div>
  );
}

export default App;
