def get_restaurants(cuisine: str):
    restaurants = {

        "pizza": [
            {"name": "Domino's", "rating": 4.5, "price": "Moderate"},
            {"name": "Pizza Hut", "rating": 4.3, "price": "Moderate"},
            {"name": "Papa John's", "rating": 4.4, "price": "Premium"}
        ],

        "burger": [
            {"name": "McDonald's", "rating": 4.2, "price": "Budget"},
            {"name": "Burger King", "rating": 4.3, "price": "Moderate"},
            {"name": "Wendy's", "rating": 4.4, "price": "Premium"}
        ],

        "south indian": [
            {"name": "A2B", "rating": 4.6, "price": "Budget"},
            {"name": "Saravana Bhavan", "rating": 4.7, "price": "Moderate"},
            {"name": "Sangeetha", "rating": 4.5, "price": "Moderate"}
        ],

        "chinese": [
            {"name": "Mainland China", "rating": 4.6, "price": "Premium"},
            {"name": "China Town", "rating": 4.3, "price": "Moderate"},
            {"name": "Beijing Bites", "rating": 4.2, "price": "Budget"}
        ]
    }

    return restaurants.get(
        cuisine.lower(),
        [{"message": "No restaurants found"}]
    )