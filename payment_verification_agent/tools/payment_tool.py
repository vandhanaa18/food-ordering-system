import random
from datetime import datetime

def verify_payment(order_id: str, amount: int):

    payment = {
        "payment_id": f"PAY{random.randint(1000,9999)}",
        "order_id": order_id,
        "amount": amount,
        "status": "Success",
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    return payment