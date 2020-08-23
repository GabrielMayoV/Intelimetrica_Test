# Intelimetrica Backend Test - Gabriel Mayo

## Overview
This repo contains the Intelimetrica test developed by Gabriel Mayo. It consists of an API for a startup called Melp, which rates restaurants according to the user data.

### Technical overview
The API is developed with Python, Django and Django REST Framework, using a PostgreSQL database and is hosted in Heroku.

## API endpoints
The base path of the API is `https://intelimetrica-test-gmv.herokuapp.com/`

### /api/restaurants/
- GET: Returns a json of the restaurants registered in the database.
- POST: Inserts a new restaurant, data is passed through the request body.
- DELETE: Deletes all the restaurants registered

### /api/restaurants/[restaurant id]
Functionality depends on the request method:
- GET: looks for the specific restaurant by id.
- PUT: updates the restaurant, new data is passed in the request body.
- DELETE: Deletes the specified restaurant


### /restaurants/statistics/[latitud]/[longitud]/[radius]/$
Delivers statistical data (number of restaurants, average rating and standard deviation rating) of the restaurants contained within the circle passed in the parameters

### Conclusions
I certainly had much fun doing this test, I hope the team likes it!
