## Introduction

This repository is my Udacity **Agentic AI (MD2)** project: a small **agent library** (Phase 1) plus a working **agentic workflow** (Phase 2) that turns an input product spec into user stories, features, and engineering tasks for the “Email Router” pilot.

## Project structure (high level)

- `src/workflow_agents/base_agents.py`: reusable agent classes (Phase 1)
- `src/*.py`: standalone scripts to run/test each agent
- `agentic_workflow.py`: Phase 2 workflow orchestration (Email Router pilot)
- `Product-Spec-Email-Router.txt`: input product specification document
- `artifacts/`: saved run outputs/logs (submission evidence)

## Setup

### Prereqs

- **Python**: `3.12` (see `.python-version`)
- **uv**: install via your preferred method (brew/pipx/etc.)

### Install dependencies (recommended: uv)

From repo root:

```bash
uv sync
```

Notes:
- Dependencies are defined in `pyproject.toml` and locked in `uv.lock`.
- You typically don’t need to manually activate a venv when using `uv run`.

### Optional: create/activate a venv (if you want one)

```bash
python -m venv .venv
source .venv/bin/activate
uv pip install -e .
```

### Environment variables (.env)

Most scripts load credentials from `tests/.env` (see `load_dotenv("tests/.env")`).

Create it:

```bash
mkdir -p tests
printf "OPENAI_API_KEY=YOUR_KEY_HERE\n" > tests/.env
```

## How to run

### Phase 2 workflow (recommended entrypoint)

From repo root:

```bash
uv run python agentic_workflow.py
```

### Run individual Phase 1 agent scripts

From repo root:

```bash
uv run python src/direct_prompt_agent.py
uv run python src/augmented_prompt_agent.py
uv run python src/knowledge_augmented_prompt_agent.py
uv run python src/rag_knowledge_prompt_agent.py
uv run python src/evaluation_agent.py
uv run python src/routing_agent.py
uv run python src/action_planning_agent.py
```

If you ever hit import issues when running by file path, run as a module instead:

```bash
uv run python -m src.direct_prompt_agent
```

## Solution overview

### Phase 1 (Agentic Toolkit)

- Implemented the reusable agent classes in `src/workflow_agents/base_agents.py`:
  - `DirectPromptAgent`
  - `AugmentedPromptAgent`
  - `KnowledgeAugmentedPromptAgent`
  - `RAGKnowledgePromptAgent`
  - `EvaluationAgent`
  - `RoutingAgent`
  - `ActionPlanningAgent`
- Added standalone run scripts under `src/` to demonstrate each agent works.

### Phase 2 (Agentic Workflow)

- Implemented `agentic_workflow.py` to orchestrate the workflow:
  - Loads `Product-Spec-Email-Router.txt`
  - Uses `ActionPlanningAgent` to generate workflow steps
  - Uses `RoutingAgent` to send each step to the right role support function:
    - Product Manager → user stories (validated by an `EvaluationAgent`)
    - Program Manager → features (validated by an `EvaluationAgent`)
    - Development Engineer → engineering tasks (validated by an `EvaluationAgent`)
  - Prints + logs the step-by-step results and final output

## Artifacts, logs, and submission evidence

- This repo exports run outputs to `artifacts/` (for evaluator evidence).
- Logging is implemented in `src/utils.py` via `export_log(...)`.
- Each script appends its output to its own log file, e.g.:
  - `artifacts/agentic_workflow.py.log`
  - `artifacts/direct_prompt_agent.py.log`
  - `artifacts/augmented_prompt_agent.py.log`
  - `artifacts/knowledge_augmented_prompt_agent.py.log`
  - `artifacts/rag_knowledge_prompt_agent.py.log`
  - `artifacts/evaluation_agent.py.log`
  - `artifacts/routing_agent.py.log`
  - `artifacts/action_planning_agent.py.log`

