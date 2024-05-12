import React, { useEffect, useState } from 'react';
import '../App.css';
import Navbar from "./Navbar";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import Home from "../pages";
import MealRequest from "../pages/meal_request.js";
import IngredientRequest from "../pages/ingredient_request.js";
import Vote from "../pages/vote.js";
import ScheduleChange from "../pages/schedule_change.js"

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/data');
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <Router>
            <Navbar />
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/meal_request" element={<MealRequest />} />
                <Route path="/ingredient_request" element={<IngredientRequest />} />
                <Route path="/vote" element={<Vote />} />
                <Route path="/schedule_change" element={<ScheduleChange />}
                />
            </Routes>
        </Router>
  );
}

export default App;