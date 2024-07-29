/*

    This is the card that represents the flight data on the home page.
    The color of the card changes according to the flight status.
    

*/


import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './flight-card.scss';
import { faClock } from '@fortawesome/free-regular-svg-icons/faClock';
import arrow from '../../assets/Arrow.png';
const FlightCard = ({ flight_number, arrival, departure, source, destination, flight_status, gate }) => {

    const border_according_to_status = () => {
        switch (flight_status) {
            case 'On Time':
                return 'rgb(79 149 79)';
            case 'Rescheduled':
                return 'rgb(161 112 22)';
            case 'Cancelled':
                return 'rgb(169 59 59)';
            case 'Boarding':
                return 'rgb(32 79 185)';
            case 'Gate Change':
                return 'rgb(114 46 203)'
        }
    }

    const difference = () => {
        const [hour_1, min_1] = arrival.split(":").map(Number);
        const [hout_2, min_2] = departure.split(":").map(Number);

        const time_1 = hour_1 * 60 + min_1;
        const time_2 = hout_2 * 60 + min_2;

        const fdifference = () => {
            if (time_1 > time_2) {
                return time_1 - time_2;
            } else {
                return time_2 - time_1;
            }
        };

        const difference = fdifference();

        const final_hr = Math.floor(difference / 60);
        const final_min = difference % 60;

        return `${String(final_hr).padStart(2, '0')}:${String(final_min).padStart(2, '0')}`;
    }

    const border_color = border_according_to_status();
    const duration = difference();

    return (
        <div className="flight-pane" style={{ border: `2px solid ${border_color}` }} >
            <div className="pane-header" style={{ background: `${border_color}` }}>
                <strong>{flight_number}</strong>
                {
                    (gate && <strong>Gate: {gate}</strong>)
                }
                <strong>{flight_status}</strong>
            </div>
            <div className="data-section">
                <div className="dept-section">
                    <span>Dep</span>
                    <p className='src'>{source}</p>
                    <span>{departure}</span>
                </div>
                <div className="divider">
                    <p className='duration'><FontAwesomeIcon icon={faClock} /> {duration}</p>
                    <div className="arrow">
                        <img src={arrow} alt="" />
                    </div>
                </div>
                <div className="arrival-section">
                    <span>Arr</span>
                    <p className='dest'>{destination}</p>
                    <span>{arrival}</span>
                </div>
            </div>
        </div>
    );
}

export default FlightCard;