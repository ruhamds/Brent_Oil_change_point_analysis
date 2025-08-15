import React, { useEffect, useState } from "react";

function App() {
  const [changePoint, setChangePoint] = useState(null);
  const [events, setEvents] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch change point results
    fetch("http://localhost:5000/api/change-point")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch change point data");
        return res.json();
      })
      .then((data) => setChangePoint(data))
      .catch((err) => setError(err.message));

    // Fetch events
    fetch("http://localhost:5000/api/events")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch events");
        return res.json();
      })
      .then((data) => setEvents(data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>🛢️ Brent Oil Change Point Detection</h1>
      {error && <p style={{ color: "red" }}>❌ Error: {error}</p>}

      {changePoint ? (
        <div>
          <h2>Change Point Data</h2>
          <pre>{JSON.stringify(changePoint, null, 2)}</pre>
        </div>
      ) : (
        <p>Loading change point data...</p>
      )}

      {events.length > 0 ? (
        <div>
          <h2>Historical Events</h2>
{events.length > 0 ? (
  events.map((event, index) => (
    <div key={index}>
      ({event.date}) - <strong>{event.event_name}</strong> ({event.event_type})
      <br />
      {event.description}
    </div>
  ))
) : (
  <p>No events found.</p>
)}
        </div>
      ) : (
        <p>Loading events...</p>
      )}
    </div>
  );
}
export default App;
