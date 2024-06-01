## Car Towing API
<p>Car Towing API allows car owners to request towing services by submitting their location information to towing companies.Car owners can quickly and easily request assistance when their vehicles get stuck.</p>


![Car Towing API](/image.png)
## Usage
1. Authentication:  Obtain an API token by authenticating as a car owner. This token will be used to authorize requests to the API. <br>

2. Submit Location: Once authenticated, submit your location information to request towing services. Include details such as: <br>
  * current location <br>
  * Model of the Car.<br>
  * Color of the car.<br>


 3. <p> Wait for Assistance: After submitting your location, wait for the towing company to respond and dispatch assistance to your location.</p>

 ## API endpoints
 `POST /auth/signup` Register as a user of the API.<br>
 `POST/auth/login`  Authenticate as a car owner stuck to obtain an API token.<br>
 `POST/tow/request` Submit your location information to request towing services <br>

 ## Authentication

 <p> To authenticate with the Car Towing API, send a POST request to /auth/login with your username and password. Upon successful authentication, you will receive an API token in the response.</p>

Examples Request:

`POST /auth/login`<br>
        {<br>
            `"username": ``"your_username",` <br>
            `"password": "your_password"`<br>
        }

Example request:
{<br>
    `"access_token": "your_access_token"` <br>
}
<p>Include the obtained access_token in the Authorization header of subsequent requests to authorize access to protected endpoints</p>


## Requesting Towing services
 <p>Send a POST request to `/tow/request`</p>

 `POST/tow/request`<br>
  { <br>
    `"location_id":"1"`<br>
  }

## Installation

Clone the repo to your local machine<br>
Navigate to project directory<br>
Create a your preferred virtual environment<br>
Install dependencies<br>
Run the App<br>
Create a .env file and generate your secret key<br>

Creating virtual env <br>
`pipenv install pipenv shell`

## License 
Distributed under the MIT License. See LICENSE for more information.

 ## Author
 Alexander Nyaga.










