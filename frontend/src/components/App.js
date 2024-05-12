import React, { useEffect, useState } from 'react';
import '../App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('/api/data');
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to React with Flask</h1>
        <p>{message}</p>
      </header>
    </div>
  );
}

export default App;