## Car Towing API
<p>Car Towing API allows car owners to request towing services by submitting their location information to towing companies.Car owners can quickly and easily request assistance when their vehicles get stuck.</p>

## Usage
1. Authentication:  Obtain an API token by authenticating as a car owner. This token will be used to authorize requests to the API. <br>

2. Submit Location: Once authenticated, submit your location information to request towing services. Include details such as: <br>
 1. current location <br>
 2. Model of the Car.<br>
 3. Color of the car.<br>


 3. <p> Wait for Assistance: After submitting your location, wait for the towing company to respond and dispatch assistance to your location.</p>

 ## API endpoints
 `POST /auth/signup` Register as a user of the API.
 `POST/auth/login`  Authenticate as a car owner stuck to obtain an API token.<br>
 `POST/tow/request` Submit your location information to request towing services <br>

 ## Authentication

 <p> To authenticate with the Car Towing API, send a POST request to /auth/login with your username and password. Upon successful authentication, you will receive an API token in the response.</p>

Examples Request:

`POST /auth/login`
        `{`
            `"username": ``"your_username",`
            `"password": "your_password"`
        `}`




