import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")


def get_nearby_restaurants(food_item: str):

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": f"{food_item} restaurant near me",
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    restaurants = []

    for place in data.get("results", [])[:5]:
        restaurants.append(place["name"])

    return restaurants