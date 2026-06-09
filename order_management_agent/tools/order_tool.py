import random

def create_order(item: str, amount: int):
    return {
        "order_id": f"ORD{random.randint(1000,9999)}",
        "item": item,
        "amount": amount
    }