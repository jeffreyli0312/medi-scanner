import { useState } from "react";

const Home = () => {
  const [blogs, setBlogs] = useState([]);
  //   let scanStatus = "Incomplete";
  const [scanStatus, setScanStatus] = useState("Incomplete");
  const handleClick = () => {
    setScanStatus("Complete");
  };

  return (
    <div className="home">
      <h2>Homepage</h2>
      <p>{scanStatus}</p>
      <button onClick={handleClick}>Click Here</button>
    </div>
  );
};

export default Home;
