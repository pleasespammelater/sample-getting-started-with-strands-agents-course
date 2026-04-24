from strands import Agent
from strands.models.bedrock import BedrockModel

model = BedrockModel(model_id="amazon.nova-pro-v1:0")
agent = Agent(model=model)
response = agent("What is Agentic AI?")
