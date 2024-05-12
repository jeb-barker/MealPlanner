import React, {useEffect} from "react";

const TicketBar = () => {

    useEffect(() => {
    fetch();
  }, []);

    let items = {};
    const fetch = async () => {
    try {
      const response = await fetch(`/api/recipes`);
      items = response.json();

    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
    return (
        <>
            {items.map(item => {

            })}
        </>
    );
};

export default TicketBar;