from google.adk.agents import Agent
from delivery_tracking_agent.prompt import DELIVERY_PROMPT
from delivery_tracking_agent.tools.tracking_tool import track_order

delivery_agent = Agent(
    name="delivery_tracking_agent",
    model="gemini-2.5-flash",
    description="Tracks food delivery status.",
    instruction=DELIVERY_PROMPT,
    tools=[track_order]
)