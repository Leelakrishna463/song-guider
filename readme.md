# Song guider - A Music Recommendation System

## Overview

This project is designed to recommend music genres and songs based on a user's mood and the current weather conditions. It utilizes machine learning models and external APIs to provide personalized recommendations.

## Features

- **Mood and Weather-Based Recommendations**: Suggests music genres and songs based on the user's mood and the weather of a specified city.
- **Machine Learning**: Uses a pre-trained KNN model to predict music genres based on energy and valence values.
- **Integration with LastFM**: Fetches top tracks for specific genres from LastFM.
- **OpenWeather API**: Retrieves current weather data for a specified city.

## Installation and Running

### Set up environment variables:
    LASTFM_API_KEY=""
    LASTFM_API_SECRET=""
    LASTFM_USERNAME=""
    LASTFM_PASSWORD=""
    OPEN_WEATHER_API_KEY=""
    API_KEY=""
    LOG_LEVEL=""
    OPEN_WEATHER_API_BASE=""

### Run the application via Docker
#### (Note: LastFM API not working because of self signed ssl certificate, use Python virutal environment instead to use host environment truststore)
1. Build docker image and run
    ```sh
    docker run -it $(docker build -q .)
    ```

### Run the application via Python Virtual environment
1. Ensure python 3.12.4 is installed from [here](https://www.python.org/downloads/)
2. Create virtual environment by below command
    ```sh
    python3.12 -m virtualenv venv
    ```
3. Activate the virtual environment
    ```sh
    source venv/bin/activate
    ```



## Usage

1. Run the FastAPI application:
    ```sh
    fastapi run app/main:app
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Testing

Run the tests using pytest:
```sh
pytest
```


# Project Documentation
https://docs.google.com/document/d/1n4KStEE8bE45HYprBs2CMXIFV81BL4bE-Jqh9VKACxA/edit#heading=h.nwfl9xbkmo3e