from google.adk.agents import Agent

from restaurant_recommendation_agent.tools.restaurant_tool import get_restaurants
from order_management_agent.tools.order_tool import create_order
from payment_verification_agent.tools.payment_tool import verify_payment
from delivery_tracking_agent.tools.tracking_tool import track_order


root_agent = Agent(
    name="food_ordering_system",
    model="gemini-2.5-flash",
    instruction="""
You are a Food Ordering Assistant.

Rules:

1. Restaurant requests:
Use get_restaurants().
Recommend suitable restaurants.

2. Order requests:
Use create_order().
Generate an order.

3. Payment requests:
Use verify_payment().
Confirm payment status.

4. Delivery requests:
Use track_order().
Provide delivery details.

Only use one tool based on the user's request.
Never answer unrelated categories.
""",
    tools=[
        get_restaurants,
        create_order,
        verify_payment,
        track_order
    ]
)