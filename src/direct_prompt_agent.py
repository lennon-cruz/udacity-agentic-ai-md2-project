# Test script for DirectPromptAgent class

# TODO: 1 - Import the DirectPromptAgent class from BaseAgents
import os
from dotenv import load_dotenv
from src.workflow_agents.base_agents import DirectPromptAgent
from src.utils import export_log

# Load environment variables from .env file
load_dotenv("tests/.env")

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key)
# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("The agent used general knowledge from the selected LLM model to generate the response.")

result = f"{direct_agent_response}\n\nThe agent used general knowledge from the selected LLM model to generate the response."
export_log("direct_prompt_agent.py", result)
