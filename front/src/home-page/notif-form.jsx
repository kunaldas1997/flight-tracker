/*

    The form to set email notification on every
    change for the flight
*/


import { useEffect, useState } from "react";
import './notif-form.scss';

const NotifForm = () => {

    const iFlightForm = {
        email: "",
        flight_number: ""
    };

    const [formData, setFormData] = useState(iFlightForm);
    const [message, setMessage] = useState('');
    const [flight, setFlight] = useState([]);
    
    // Form function to handle changes
    const assignChanges = (event) => {
        const { name, value } = event.target;
        setFormData((previous) => ({
            ...previous,
            [name]: value
        }));
    };

   

    // Form submit function
    const sendData = (e) => {
        e.preventDefault();
        const json = JSON.stringify(formData);

        fetch('http://localhost:5000/create_notif', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: json
        })
            .then((response) => response.json())
            .then((data) => {
                setMessage(data.message);
                setFormData(iFlightForm); // Reset form data
                setTimeout(() => { // reset message
                    setMessage('');
                }, 5000);
            })
            .catch((error) => {
                console.error('Error: ', error);
            });
    };


    return (
        <div className="notif-form">
            <div className="notif-form-head">
                <p className="title">Track your Flight</p>
            </div>
            <form onSubmit={sendData}>
                <div className="email">
                    <input type="email" name="email" value={formData.email} onChange={assignChanges} placeholder="Email" autoComplete="false" />
                </div>
                <div className="flight">
                    <input type="text" name="flight_number" value={formData.flight_number} onChange={assignChanges} placeholder="Flight Number" autoComplete="false" />
                </div>
                <button type="submit">Submit</button>
            </form>

            {message && <div className="message">{message}</div>}
        </div>
    )
}

export default NotifForm