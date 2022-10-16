import "./App.css";
import Navbar from "./Navbar";
import Home from "./Home";
import InjuryList from "./InjuryList";
import axios from "axios";
import React, { Component } from "react";
import ImageUploading from "react-images-uploading";
// eslint-disable-next-line

class App extends Component {
  state = {
    selectedFile: null,
  };

  fileSelectedHandler = (event) => {
    this.setState({});
  };

  fileUploadHandler = () => {
    const fd = new FormData();
    fd.append(
      "image",
      this.state.selectedFile,
      this.state.selectedFile.className
    );
    axios
      .post("http://127.0.0.1:5000/my-link2/", fd, {
        onUploadProgress: (progressEvent) =>
          console.log(
            "Upload Progress: " +
              Math.round((progressEvent.loaded / progressEvent.total) * 100) +
              "%"
          ),
      })
      .then((res) => {
        console.log(res);
      });
  };
  // need api endpoint to store files in a storage or db
  //   .then(res =>{
  //     console.log(res);
  //   }
  // });

  render() {
    return (
      <div className="App">
        <Navbar />
        <div className="content">
          <Home />
        </div>
        <input type="file" onChange={this.fileSelectedHandler} />
        <button onClick={this.fileUploadHandler}>Upload</button>
      </div>
    );
  }
}
export default App;
