def get_restaurants(cuisine: str):
    restaurants = {
        "pizza": ["Domino's", "Pizza Hut"],
        "burger": ["McDonald's", "Burger King"],
        "south indian": ["A2B", "Saravana Bhavan"]
    }

    return restaurants.get(cuisine.lower(), ["No restaurants found"])