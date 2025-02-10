import React, { useState, useEffect } from "react";
import "./styles.css"; // Import styles


const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

function App() {
  const [data, setData] = useState([]);
  const [query, setQuery] = useState("");

  const handleSearch = () => {
    fetch(`${API_URL}/search?q=${query}`)
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error("Error fetching data:", error));
  };

  return (
    <div>
      <h1>📡 Cable List Search</h1>
      <input
        type="text"
        placeholder="Leitaðu eftir kapalnúmeri..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      <ul>
        {data.length > 0 ? (
          data.map((item, index) => (
            <li key={index}>
              {item.column1} - {item.column2}
            </li>
          ))
        ) : (
          <p>No data found.</p>
        )}
      </ul>
    </div>
  );
}

export default App;
