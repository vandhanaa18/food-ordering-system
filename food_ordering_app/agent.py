from google.adk.agents import Agent

from restaurant_recommendation_agent.agent import restaurant_agent
from order_management_agent.agent import order_agent
from payment_verification_agent.agent import payment_agent
from delivery_tracking_agent.agent import delivery_agent


root_agent = Agent(
    name="food_ordering_system",
    model="gemini-2.5-flash",
    instruction="""
You are a Food Ordering Assistant.

Delegate restaurant recommendations to the Restaurant Agent.

Delegate order creation and management to the Order Agent.

Delegate payment verification to the Payment Agent.

Delegate delivery tracking to the Delivery Agent.
""",
    sub_agents=[
        restaurant_agent,
        order_agent,
        payment_agent,
        delivery_agent
    ]
)