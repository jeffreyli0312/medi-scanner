import "./App.css";
import Navbar from "./Navbar";
import Home from "./Home";
import InjuryList from "./InjuryList";
import axios from "axios";
import React, { Component } from "react";
import ImageUploading from "react-images-uploading";
// // eslint-disable-next-line

// class App extends Component {
//   state = {
//     selectedFile: null,
//   };

//   fileSelectedHandler = (event) => {
//     this.setState({});
//   };

//   fileUploadHandler = () => {
//     const fd = new FormData();
//     fd.append(
//       "image",
//       this.state.selectedFile,
//       this.state.selectedFile.className
//     );
//     axios
//       .post("http://127.0.0.1:5000/my-link2/", fd, {
//         onUploadProgress: (progressEvent) =>
//           console.log(
//             "Upload Progress: " +
//               Math.round((progressEvent.loaded / progressEvent.total) * 100) +
//               "%"
//           ),
//       })
//       .then((res) => {
//         console.log(res);
//       });
//   };
//   // need api endpoint to store files in a storage or db
//   //   .then(res =>{
//   //     console.log(res);
//   //   }
//   // });

//   render() {
//     return (
//       <div className="App">
//         <Navbar />
//         <div className="content">
//           <Home />
//         </div>
//         <input type="file" onChange={this.fileSelectedHandler} />
//         <button onClick={this.fileUploadHandler}>Scan This Image</button>
//       </div>
//     );
//   }
// }
// export default App;

// import axios from "axios";

// import React, { Component } from "react";

class App extends Component {
  state = {
    // Initially, no file is selected
    selectedFile: null,
  };

  // On file select (from the pop up)
  onFileChange = (event) => {
    // Update the state
    this.setState({ selectedFile: event.target.files[0] });
  };

  // On file upload (click the upload button)
  onFileUpload = () => {
    // Create an object of formData
    const formData = new FormData();

    // Update the formData object
    formData.append(
      "myFile",
      this.state.selectedFile,
      this.state.selectedFile.name
    );

    // Details of the uploaded file
    console.log(this.state.selectedFile);

    // Request made to the backend api
    // Send formData object
    axios.post("http://127.0.0.1:5000/my-link2/", formData)
  };

  // File content to be displayed after
  // file upload is complete
  fileData = () => {
    if (this.state.selectedFile) {
      return (
        <div>
          <h2>File Details:</h2>

          <p>File Name: {this.state.selectedFile.name}</p>

          <p>File Type: {this.state.selectedFile.type}</p>

          <p>
            Last Modified:{" "}
            {this.state.selectedFile.lastModifiedDate.toDateString()}
          </p>
        </div>
      );
    } else {
      return (
        <div>
          <br />
          <h4>Choose before Pressing the Upload button</h4>
        </div>
      );
    }
  };

  render() {
    return (
      <div>
        <Navbar />
        <div className="App">
          <Home />
          <div>
            <input type="file" onChange={this.onFileChange} />
            <button onClick={this.onFileUpload}>View Scanner</button>
          </div>
          {this.fileData()}
        </div>
      </div>
    );
  }
}

export default App;
