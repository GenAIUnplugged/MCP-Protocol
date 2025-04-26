import httpx
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp import Context

# Initialize the MCP server
mcp = FastMCP("CityWeatherServer")

@mcp.tool()
async def get_city_weather(city: str) -> str:
    """
    Fetches current weather information for a given city using Open-Meteo API.
    """
    # Step 1: Geocode the city name to get latitude and longitude
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    async with httpx.AsyncClient() as client:
        geo_response = await client.get(geocode_url)
        if geo_response.status_code != 200:
            return f"Error fetching geocoding data: {geo_response.text}"
        geo_data = geo_response.json()
        results = geo_data.get("results")
        if not results:
            return f"City '{city}' not found."
        lat = results[0]["latitude"]
        lon = results[0]["longitude"]

        # Step 2: Get current weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = await client.get(weather_url)
        if weather_response.status_code != 200:
            return f"Error fetching weather data: {weather_response.text}"
        weather_data = weather_response.json()
        current = weather_data.get("current_weather", {})
        temperature = current.get("temperature")
        windspeed = current.get("windspeed")
        winddirection = current.get("winddirection")
        weathercode = current.get("weathercode")

        return (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Wind Speed: {windspeed} km/h\n"
            f"Wind Direction: {winddirection}°\n"
            f"Weather Code: {weathercode}"
        )

# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
