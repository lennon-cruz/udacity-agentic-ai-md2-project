import os
import sys
from dotenv import load_dotenv
from src.workflow_agents.base_agents import RAGKnowledgePromptAgent
from src.utils import export_log

# Load environment variables from .env file (try multiple locations)
load_dotenv("tests/.env")

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    print("ERROR: OPENAI_API_KEY not found in environment variables!")
    print("Please create a .env file with OPENAI_API_KEY=your_key_here")
    sys.exit(1)

persona = "You are a college professor, yous answer always starts with: Dear students,"
print("✓ Initializing Agent...")
# Note: chunk_size=500, chunk_overlap=50 (reduced from 200 to avoid infinite loop issues)
# Overlap should be much smaller than chunk_size (typically 10-20% of chunk_size)
try:
    RAG_knowledge_prompt_agent = RAGKnowledgePromptAgent(openai_api_key, persona, chunk_size=500, chunk_overlap=50)
    print("✓ Agent initialized successfully")
except Exception as e:
    print(f"ERROR initializing agent: {e}")
    sys.exit(1)

knowledge_text = """
In the historic city of Boston, Clara, a marine biologist and science communicator, began each morning analyzing sonar data to track whale migration patterns along the Atlantic coast.
She spent her afternoons in a university lab, researching CRISPR-based gene editing to restore coral reefs damaged by ocean acidification and warming.
Clara was the daughter of Ukrainian immigrants—Olena and Mykola—who fled their homeland in the late 1980s after the Chernobyl disaster brought instability and fear to their quiet life near Kyiv.

Her father, Mykola, had been a radio engineer at a local observatory, skilled in repairing Soviet-era radio telescopes and radar systems that tracked both weather patterns and cosmic noise.
He often told Clara stories about jury-rigging radio antennas during snowstorms and helping amateur astronomers decode signals from distant pulsars.
Her mother, Olena, was a physics teacher with a hidden love for poetry and dissident literature. In the evenings, she would read from both Ukrainian folklore and banned Western science fiction.
They survived harsh winters, electricity blackouts, and the collapse of the Soviet economy, but always prioritized education and storytelling in their home.
Clara’s childhood was shaped by tales of how her parents shared soldering irons with neighbors, built makeshift telescopes, and taught physics to students with no textbooks but endless curiosity.

Inspired by their resilience and thirst for knowledge, Clara created a podcast called **"Crosscurrents"**, a show that explored the intersection of science, culture, and ethics.
Each week, she interviewed researchers, engineers, artists, and activists—from marine ecologists and AI ethicists to digital archivists preserving endangered languages.
Topics ranged from brain-computer interfaces, neuroplasticity, and climate migration to LLM prompt engineering, decentralized identity, and indigenous knowledge systems.
In one popular episode, she explored how retrieval-augmented generation (RAG) could help scientific researchers find niche studies buried in decades-old journals.
In another, she interviewed a Ukrainian linguist about preserving dialects lost during the Soviet era, drawing parallels to language loss in marine mammal populations.

Clara also used her technical skills to build Python-based dashboards that visualized ocean temperature anomalies and biodiversity loss, often collaborating with her best friend Amir, a data engineer working on smart city infrastructure.
Together, they discussed smart grids, blockchain for sustainability, quantum encryption, and misinformation detection in synthetic media.
At a dockside café near Boston Harbor, they often debated the ethical implications of generative AI, autonomous weapons, and the carbon footprint of LLM training runs.

In quieter moments, Clara translated traditional Ukrainian embroidery patterns into generative AI art, donating proceeds to digital archives preserving Eastern European culture.
She contributed to open-source projects involving semantic search, vector databases, and multimodal embeddings—often experimenting with few-shot learning and graph-based retrieval techniques to improve her podcast's episode discovery engine.

One night, while sharing homemade borscht, Clara told Amir how her grandparents once used Morse code to transmit encrypted weather updates through the Carpathian Mountains during World War II.
The story sparked a conversation about ancient navigation, space weather interference with submarine cables, and the neuroscience behind why humans create myths to understand uncertainty.

To Clara, knowledge was a living system—retrieved from the past, generated in the present, and evolving toward the future.
Her life and work were testaments to the power of connecting across disciplines, borders, and generations—exactly the kind of story that RAG models were born to find.
"""

print("\n✓ Chunking knowledge text...")
print(f"  Text length: {len(knowledge_text)} characters")
print(f"  Chunk size: {RAG_knowledge_prompt_agent.chunk_size}, Overlap: {RAG_knowledge_prompt_agent.chunk_overlap}")
try:
    chunks = RAG_knowledge_prompt_agent.chunk_text(knowledge_text)
    print(f"✓ Created {len(chunks)} chunks")
    print(f"  Chunk file: chunks-{RAG_knowledge_prompt_agent.unique_filename}")
except Exception as e:
    print(f"ERROR during chunking: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n✓ Calculating embeddings (this may take a while - making API calls for each chunk)...")
try:
    embeddings = RAG_knowledge_prompt_agent.calculate_embeddings()
    print(f"✓ Calculated embeddings for {len(embeddings)} chunks")
    print(f"  Embeddings file: embeddings-{RAG_knowledge_prompt_agent.unique_filename}")
except Exception as e:
    print(f"ERROR during embedding calculation: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

prompt = "What is the podcast that Clara hosts about?"
print(f"\n✓ Processing prompt: {prompt}")
print("*"*50)
try:
    prompt_answer = RAG_knowledge_prompt_agent.find_prompt_in_knowledge(prompt)
    print("\nResponse:")
    print(prompt_answer)
    export_log("rag_knowledge_prompt_agent.py", f"prompt: {prompt}\n{'*'*50}\nResponse:\n{prompt_answer}")
except Exception as e:
    print(f"ERROR during prompt processing: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)