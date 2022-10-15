const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Medi-Scanner</h1>
      <div className="links">
        <a href="/">Home</a>
        <a
          href="/upload"
          style={{
            color: "white",
            backgroundColor: "#f1356d",
            borderRadius: "8px",
          }}
        >
          Upload
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
