 Weather Application using Django

## Overview
This Django-based weather application provides users with current weather information for a given location. Users can search for weather details by entering the city name, and the application will fetch and display the latest weather data.

## Features
- Current weather information display
- City-based weather search
- Responsive design for various devices
- Weather data sourced from a reliable API

## Setup Instructions

### Prerequisites
- Python 3.x installed
- Django installed (`pip install Django`)
- API key from a weather data provider (e.g., OpenWeatherMap)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app-django.git
   cd weather-app-django
Install dependencies:

pip install -r requirements.txt
## Configure API Key:

Sign up for a free API key from a weather data provider (e.g., OpenWeatherMap).
Create a file named .env in the project root and add your API key:

WEATHER_API_KEY=your_api_key_here
## Apply migrations:

python manage.py migrate

## Run the development server:

python manage.py runserver
Open your browser and navigate to http://localhost:8000 to access the weather application.

## Configuration
Environment Variables
WEATHER_API_KEY: Your API key for accessing weather data.
Project Structure
weather_app/: Django application folder.
templates/: HTML templates for rendering views.
static/: Static files (CSS, JS, images, etc.).
requirements.txt: List of Python dependencies.
