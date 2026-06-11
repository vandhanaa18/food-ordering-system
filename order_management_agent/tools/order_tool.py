import random


menu = {
    "veg pizza": 350,
    "farmhouse pizza": 450,
    "burger": 200,
    "coke": 50,
    "french fries": 120,
    "fried rice": 220,
    "south indian meal": 180
}


order_history = []


def create_order(item: str, quantity: int = 1):

    item = item.lower()

    # Automatically add new dishes if not present
    if item not in menu:
        menu[item] = random.randint(100, 500)

    amount = menu[item] * quantity

    order = {
        "order_id": f"ORD{random.randint(1000, 9999)}",
        "item": item.title(),
        "quantity": quantity,
        "amount": amount
    }

    order_history.append(order)

    return order


def show_order_history():
    return order_history


def update_order(order_id, new_quantity):

    for order in order_history:

        if order["order_id"] == order_id:

            order["quantity"] = new_quantity
            order["amount"] = (
                menu[order["item"].lower()] * new_quantity
            )

            return {
                "message": "Order updated successfully",
                "order": order
            }

    return {
        "message": "Order not found"
    }


def cancel_order(order_id):

    for order in order_history:

        if order["order_id"] == order_id:

            order_history.remove(order)

            return {
                "message": "Order cancelled successfully"
            }

    return {
        "message": "Order not found"
    }
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def get_food_variants(food_item: str):

    prompt = f"""
    A customer wants {food_item}.

    Suggest 5 popular varieties of this food with realistic Indian prices in India.

    Format:

    1. Name - ₹Price
    2. Name - ₹Price

    Only return the list.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text