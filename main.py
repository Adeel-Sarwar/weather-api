from fastapi import FastAPI
import aiohttp
import requests_cache
from datetime import timedelta

app = FastAPI(title="Weather API")
requests_cache.install_cache('weather_cache', expire_after=timedelta(minutes=10))
apiKey = "your_openweathermap_api_key"

async def fetch_weather_data(city: str, api_key: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Error: {response.status}")

async def fetch_forecast_data(city: str, api_key: str):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return [entry for entry in data['list'][:3]]
            else:
                raise Exception(f"Error: {response.status}")

@app.get("/weather/{city}")
async def get_weather(city: str):
    try:
        weather_data = await fetch_weather_data(city, apiKey)
        forecast_data = await fetch_forecast_data(city, apiKey)
        return {
            "city": city,
            "current": {
                "temperature": weather_data["main"]["temp"],
                "description": weather_data["weather"][0]["description"],
                "humidity": weather_data["main"]["humidity"]
            },
            "forecast": [{"time": f["dt_txt"], "temp": f["main"]["temp"], "desc": f["weather"][0]["description"]} for f in forecast_data]
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)