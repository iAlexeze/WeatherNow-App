from flask import Flask, render_template, request, jsonify
from werkzeug.serving import run_simple
import json
import redis
import requests
from dotenv import load_dotenv
import os
import traceback


app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure Redis
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)
CACHE_EXPIRATION = 2000  # Cache expiration time in seconds


def print_redis_connection():
    print(f"Connected to Redis on {redis_host}:{redis_port}")


def create_weather_url(location):
    api_key = os.getenv('WEATHERAPI_API_KEY')
    return f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        response = get_weather_response(location)
        return render_template('index.html', response=response)

    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.json['location']
    unit = request.json['unit']

    weather_info = get_weather_response(location)
    if isinstance(weather_info, dict):
        if unit == 'fahrenheit':
            weather_info['temperature'] = convert_to_fahrenheit(weather_info['temperature'])
            weather_info['unit'] = 'fahrenheit'

        return jsonify(weather_info), 200
    else:
        return jsonify({'error': weather_info}), 500


def get_weather_response(location):
    print(f"Getting weather data for {location}...")
    # Check if the weather data is cached in Redis
    cached_data = redis_client.get(location)
    if cached_data:
        print(f"Retrieving weather data for {location} from cache...")
        return json.loads(cached_data)

    try:
        # Make a real API call to WeatherAPI
        weather_url = create_weather_url(location)
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()  # Raise an exception for non-2xx status codes
        weather_data = weather_response.json()

        if 'error' in weather_data:
            return f"Unable to retrieve weather data for {location}"

        # Extract relevant weather information from the response
        weather_info = {
            "location": location,
            "temperature": str(weather_data['current']['temp_c']),
            "unit": "celsius",
            "forecast": [weather_data['current']['condition']['text']],
        }

        # Cache the weather data in Redis for future use
        redis_client.setex(location, CACHE_EXPIRATION, json.dumps(weather_info))

        return weather_info

    except Exception as e:
        traceback.print_exc()  # Print the full traceback
        return f"An error occurred while retrieving weather data for {location}"


if __name__ == '__main__':
    print_redis_connection()
    app.run('localhost', 5000, debug=True)
