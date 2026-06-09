import random

def track_delivery(order_id: str):

    partners = [
        "Rahul",
        "Arun",
        "Priya",
        "Kiran",
        "Vijay",
        "Anitha"
    ]

    stages = [
        "Order Confirmed",
        "Preparing Food",
        "Out for Delivery",
        "Delivered"
    ]

    return {
        "order_id": order_id,
        "status": random.choice(stages),
        "delivery_partner": random.choice(partners),
        "eta": f"{random.randint(10,40)} minutes"
    }