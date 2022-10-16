import React from "react";
const InjuryList = ({ injury, title, handleDelete }) => {
  return (
    <div className="injury-list">
      <h2>{title}</h2>
      {injury.map((injury) => (
        <div className="injury-preview" key={injury.id}>
          <h2>{injury.title}</h2>
          <button onClick={() => handleDelete(injury.id)}>delete injury</button>
        </div>
      ))}
    </div>
  );
};

export default InjuryList;
