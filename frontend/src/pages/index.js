import React from "react";
import "../Home.css"
import Calendar from 'react-calendar'
import TicketBar from '../components/TicketBar.js'
import 'react-calendar/dist/Calendar.css';

const Home = () => {
    let date = new Date();
    let firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
    let lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);

    const mealDays = async () => {
    try {
      const response = await fetch(`/api/meal_days?json={start:${firstDay},end:${lastDay}}`);
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

    let enableOnlyMealDays = function ({ activeStartDate, date, view }) {
        return true;
    }
    return (
        <div className={"home"}>
            <h1>Welcome to the Meal Planner</h1>
            <h4>Take a look at the meal schedule below, or submit a ticket with one of the buttons at the top of the screen</h4>
            <div className={ticket_bar}>
                <TicketBar></TicketBar>
            </div>
            <div className={calendar}>
                <Calendar activeStartDate={firstDay} tileDisabled={enableOnlyMealDays}></Calendar>
            </div>
        </div>
    );
};

export default Home;