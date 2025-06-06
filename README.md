# Weather API
An advanced Python RESTful API that provides real-time weather data and short-term forecasts.
## Features
- Fetches current weather and 3-period forecast using OpenWeatherMap
- Asynchronous requests for efficiency
- Data caching to reduce API calls
- Error handling for robust performance
## Screenshots
![Server Running](screenshots/server_running.png)
![API Response](screenshots/api_response.png)
## How to Run
1. Install dependencies: `pip install fastapi uvicorn aiohttp requests-cache`
2. Replace "your_openweathermap_api_key" with your OpenWeatherMap API key
3. Run `uvicorn main:app --reload`