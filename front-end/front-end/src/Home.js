import React, { useState } from "react";
import InjuryList from "./InjuryList";

const Home = () => {
  const [injury, setInjurys] = useState([
    { title: "Skin Burn", body: "lorem ipsum...", id: 1 },
    // { title: "Bruises", body: "lorem ipsum...", id: 2 },
    // { title: "Cuts", body: "lorem ipsum...", id: 3 },
  ]);

  const handleDelete = (id) => {
    const newInjurys = injury.filter((injury) => injury.id !== id);
    setInjurys(newInjurys);
  };

  return (
    <div className="home">
      <InjuryList
        injury={injury}
        title="All Injuries"
        handleDelete={handleDelete}
      />
    </div>
  );
};

export default Home;
