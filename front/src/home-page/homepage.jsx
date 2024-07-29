/*
    Homepage of the website.
    Refreshes data every 3sec
*/


import { useEffect, useState } from "react";
import FlightCard from "./flightcard/flight-card";
import "./homepage.scss"


const HomePage = () => {
    const [getflights, setFlightData] = useState([])
    const [loading, setLoading] = useState(true);
    const [message, setMessage] = useState(null)

    useEffect(() => {
        let isMounted = true;

        const fetchData = () => {
            fetch('http://localhost:5000/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Not Ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (isMounted) {
                        setFlightData(data);
                        setLoading(false);
                    }
                })
                .catch(error => {
                    if (isMounted) {
                        setMessage(error.message);
                        setLoading(false);
                    }
                });
        };

        fetchData();

        const interval = setInterval(fetchData, 10000 / 3);

        return () => {
            isMounted = false;
            clearInterval(interval);
        };
    }, []);


    if (loading) {
        return <div>Loading...</div>
    }
    if (message) {
        return <div>Error:  {message}</div>
    }
    
    return (
        <div className="data">
            {
                getflights.map(flight => (
                    <FlightCard
                        key={flight._id}
                        flight_number={flight.flight_number}
                        flight_status={flight.status}
                        source={flight.src}
                        destination={flight.dest}
                        departure={flight.dept}
                        arrival={flight.arr}
                        gate={flight.gate} />
                ))
            }
        </div>
    );
}

export default HomePage;