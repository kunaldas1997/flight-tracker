# Project Title

## Summary

Flight Tracker is a simple flight tracking web application, which allows user to subscribe to their flight, and receive email in the real-time. Also, it lets the user to check all flight status in the realtime. 
It has an API meant for admin purposes to feed in data. 
There are three database/collection used:
- **Topic:** Holds the flight number along with its respective user email ID
 **Flight:** Holds all flight data
 **User:** For holding admin accounts only (for now)

Flow:
- To add flight data, admin needs to use tools like Postman to sign up, sign in and get access token to further add/update flights
- Passenger can check the real-time status of all flights.
- Passenger needs to add their email and Flight number in the given form to get email.
- Passenger gets email once the admin update data. 


Note:
- Please go through the comments in the files, especially in the `send_email.py` to setup your own MailGun API.
- For MailGun, you have to register the email address, using which you want to send the email from.
- API key and API url is also needed.
- 
## Tech Stack

- **Language:**
  - Python
  - JavaScript

- **Backend:**
  - **Python Framework and Libraries:**
    - `flask` (a lightweight web framework)
    - `flask_jwt_extended` (for JWT authentication)
    - `hashlib`
    - `bson`
    - `pymongo` (for MongoDB interaction)

- **Frontend:**
  - **JavaScript Framework and Libraries:**
    - Reactjs
    - Font Awesome
  - **Builder and Environment:**
    - Vite
  - **Pre-processor:**
    - Sass

- **Database:**
  - MongoDB

- **Tools:**
  - **API Manipulation:**
    - POSTMAN
  - **MongoDB Visualization:**
    - MongoDB Compass
  - **Code Editor:**
    - VSCode
