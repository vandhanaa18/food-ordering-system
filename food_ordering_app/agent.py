from google.adk.agents import Agent

from restaurant_recommendation_agent.tools.restaurant_tool import (
    get_nearby_restaurants
)

from payment_verification_agent.tools.payment_tool import (
    verify_payment
)

from delivery_tracking_agent.tools.tracking_tool import (
    track_delivery
)

from order_management_agent.agent import order_agent


root_agent = Agent(
    name="food_ordering_system",
    model="gemini-2.5-flash",
    instruction="""
You are a Food Ordering Assistant.

Rules:

1. Restaurant requests:
Use get_nearby_restaurants().
Recommend suitable restaurants.

2. Order requests:
Delegate all order-related tasks to order_management_agent.
Do NOT directly create orders.

3. Payment requests:
Use verify_payment().

4. Delivery requests:
Use track_delivery().

Only use one category at a time.
""",

    tools=[
        get_nearby_restaurants,
        verify_payment,
        track_delivery
    ],

    sub_agents=[
        order_agent
    ]
)