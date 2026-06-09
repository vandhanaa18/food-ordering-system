from google.adk.agents import Agent
from .prompt import ORDER_PROMPT

order_agent = Agent(
    name="order_management_agent",
    model="gemini-2.5-flash",
    description="Order Management Agent",
    instruction=ORDER_PROMPT,
    tools=[create_order]
)