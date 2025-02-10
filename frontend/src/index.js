import React from "react";
import ReactDOM from "react-dom/client"; // ✅ Use createRoot from React 18
import App from "./App";
import "./styles.css"; // ✅ Ensure styles are imported

const root = ReactDOM.createRoot(document.getElementById("root")); // ✅ Use createRoot
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
