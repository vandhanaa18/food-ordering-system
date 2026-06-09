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

    if item not in menu:
        return {
            "error": "Item not available"
        }

    amount = menu[item] * quantity

    order = {
        "order_id": f"ORD{random.randint(1000,9999)}",
        "item": item,
        "quantity": quantity,
        "amount": amount
    }

    order_history.append(order)

    return order


def show_order_history():
    return order_history