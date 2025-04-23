from google.adk.agents import Agent
from .tools import generate_hashtags

root_agent = Agent(
    name="hashtag_generator",
    model="gemini-1.5-flash-002",
    instruction="Generate relevant and popular hashtags based on the caption and image description provided.",
    description="An agent that suggests hashtags for social media posts.",
    tools=[generate_hashtags],
)
