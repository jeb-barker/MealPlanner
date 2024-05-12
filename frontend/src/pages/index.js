import React from "react";
import "../Home.css"
import Calendar from 'react-calendar'
import 'react-calendar/dist/Calendar.css';

const Home = () => {
    return (
        <div className={"home"}>
            <h1>Welcome to the Meal Planner</h1>
            <h4>Take a look at the meal schedule below, or submit a ticket with one of the buttons at the top of the screen</h4>
            <Calendar></Calendar>
        </div>
    );
};

export default Home;