import { useState } from "react";
import InjuryList from "./InjuryList";

const Home = () => {
  const [injury, setinjury] = useState([
    {
      title: "Skin Burn",
      body: "lorem ipsum...",
      author: "Medi-Scanner",
      id: 1,
    },
    { title: "Bruises", body: "lorem ipsum...", author: "Medi-Scanner", id: 2 },
    {
      title: "Cuts",
      body: "lorem ipsum...",
      author: "Medi-Scanner",
      id: 3,
    },
  ]);

  return (
    <div className="home">
      <InjuryList injury={injury} title="All Injuries " />
    </div>
  );
};

export default Home;
