import React, { useState, useEffect } from "react";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/search?q=test`)
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>📡 Cable List Search</h1>
      <p>Fetching data from {API_URL}...</p>
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
