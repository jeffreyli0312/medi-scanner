const InjuryList = ({ injury, title }) => {
  // const injury = props.injury;
  // const title = props.title;
  // console.log(injury);

  return (
    <div className="injury-list">
      <h2>{title}</h2>
      {injury.map((injury) => (
        <div className="injury-preview" key={injury.id}>
          <h2>{injury.title}</h2>
          <p>Powered by {injury.author}</p>
        </div>
      ))}
    </div>
  );
};

export default InjuryList;
