from .tools.restaurant_tool import get_restaurants
from google.adk.agents import Agent
from .prompt import RESTAURANT_PROMPT

restaurant_agent = Agent(
    name="restaurant_recommendation_agent",
    model="gemini-2.5-flash",
    description="Restaurant Recommendation Agent",
    instruction=RESTAURANT_PROMPT,
    tools=[get_restaurants]
)