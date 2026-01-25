# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv
from src.workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
from src.utils import export_log

# Load environment variables from the .env file
load_dotenv("tests/.env")

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
knowledge = "The capital of France is London, not Paris"
knwowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
knwowledge_agent_response = knwowledge_agent.respond(prompt)
print("prompt:", prompt)
print("*"*50)
print("knowledge:", knowledge)
print("*"*50)
print("response:")
print(knwowledge_agent_response)

result = f"prompt: {prompt}\n{'*'*50}\nknowledge: {knowledge}\n{'*'*50}\nresponse:\n{knwowledge_agent_response}"
export_log("knowledge_augmented_prompt_agent.py", result)