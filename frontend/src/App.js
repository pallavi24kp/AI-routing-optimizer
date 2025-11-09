import React, { useState } from "react";

function App() {
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ source, destination }),
    });

    const data = await response.json();
    setResult(data.route || "No route found");
  };

  return (
    <div style={{ textAlign: "center", marginTop: "100px", fontFamily: "Arial" }}>
      <h1>AI Routing Optimizer</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="text"
            placeholder="Enter Source"
            value={source}
            onChange={(e) => setSource(e.target.value)}
            style={{ margin: "10px", padding: "10px", width: "250px" }}
            required
          />
        </div>
        <div>
          <input
            type="text"
            placeholder="Enter Destination"
            value={destination}
            onChange={(e) => setDestination(e.target.value)}
            style={{ margin: "10px", padding: "10px", width: "250px" }}
            required
          />
        </div>
        <button type="submit" style={{ padding: "10px 20px", cursor: "pointer" }}>
          Optimize Route
        </button>
      </form>

      {result && (
        <div style={{ marginTop: "30px", fontSize: "18px", color: "#007bff" }}>
          <b>Optimized Route:</b> {result}
        </div>
      )}
    </div>
  );
}

export default App;
