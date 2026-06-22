# AI Research Agent with Self-Reflection and Tool-Use (LangGraph + LangChain)

##  Overview

This project is an experimental **AI research agent** built using **LangChain, LangGraph, and OpenAI tool calling**. It is designed to answer complex research questions by generating structured responses, reflecting on its own output, retrieving external information, and iteratively improving its answers.

Instead of producing a single static response, the system behaves like an **agentic workflow** that:

- Generates an initial answer  
- Critically evaluates its own response  
- Produces search queries for missing information  
- Uses web search (Tavily API) to retrieve external data  
- Revises and improves the final answer  
- Enforces structured outputs using Pydantic schemas  

The goal of this project is to explore **advanced LLM orchestration patterns and agent design principles**.

---

##  Key Features

-  Multi-step reasoning pipeline (Draft → Reflect → Revise)
-  Self-critique and reflection mechanism
-  Web search integration using Tavily API
-  Structured tool calling with OpenAI function tools
-  LangGraph state-based orchestration
-  Pydantic-validated structured outputs
-  Iterative improvement loop with stopping conditions
-  Citation-aware answer refinement

---

##  System Architecture


User Question
↓
Draft Node (Initial Answer Generation)
↓
Tool Execution (Tavily Web Search)
↓
Revise Node (Improved Answer + Citations)
↓
Conditional Loop (Iteration Control)
↓
Final Answer Output


---

##  Core Concepts Learned

### 1. Agentic AI Design
This project demonstrates how to build autonomous LLM agents that can:
- Plan responses
- Use tools
- Reflect on outputs
- Improve iteratively

---

### 2. Structured LLM Outputs (Pydantic + Tool Calling)
Instead of free-form text, responses are structured using schemas:

- `AnswerQuestion`
- `ReviseAnswer`
- `Reflection`

This enables:
- Reliable parsing
- Deterministic workflows
- Stronger orchestration control

---

### 3. Self-Reflection Loop
The model evaluates its own output by:
- Identifying missing information
- Detecting unnecessary content
- Generating search queries for improvement

This creates a **feedback loop similar to human reasoning**.

---

### 4. Tool-Augmented LLMs
The system integrates external tools:

- Tavily Search API for real-time information
- LangChain StructuredTool
- LangGraph ToolNode

This allows the model to ground responses in real-world data instead of hallucinating.

---

### 5. LangGraph State Machines
The workflow is implemented as a state graph where:

- Nodes represent reasoning steps
- Edges represent transitions
- Conditional logic controls iteration flow

This is a modern pattern for building **LLM agents as executable programs**.

---

### 6. Iteration Control
To prevent infinite loops, the system:

- Tracks tool usage via `ToolMessage`
- Limits execution using `MAX_ITERATIONS`
- Stops execution when threshold is reached

---

##  Project Structure


.
├── chains.py # LLM prompts, reasoning chains, tool binding
├── schemass.py # Pydantic schemas for structured outputs
├── tool_executor.py # Tavily search tool integration
├── main.py # LangGraph workflow orchestration


---

##  Technologies Used

- Python 3.10+
- LangChain
- LangGraph
- OpenAI GPT-4 Turbo
- Tavily Search API
- Pydantic
- python-dotenv

---

##  How It Works

### 1. Draft Phase
The model generates an initial ~250-word structured answer.

### 2. Reflection Phase
It critiques its own response:
- Missing information
- Overly verbose or irrelevant content

### 3. Search Query Generation
The model produces queries to improve the answer.

### 4. Tool Execution
Tavily search retrieves relevant external sources.

### 5. Revision Phase
The model rewrites the answer using:
- Critique feedback
- External search results
- Citation requirements

### 6. Final Output
A refined, structured, and more accurate response is produced.

---

##  Example Use Case

Example query:

> "Write about AI-powered SOC / autonomous SOC startups and funding"

The system:
- Generates an initial overview
- Identifies missing companies and funding data
- Searches the web for additional context
- Produces an improved, more complete final answer

---

##  What I Learned

This project helped me understand and implement:

- Building **agentic AI systems beyond simple chatbots**
- Designing **multi-step LLM reasoning pipelines**
- Using **LangGraph for state machine orchestration**
- Implementing **tool-augmented LLM architectures**
- Structuring outputs with **Pydantic + OpenAI tools**
- Creating **self-reflective AI loops**
- Managing iterative execution safely
- Integrating external APIs into LLM workflows

---

##  Future Improvements

- Add long-term memory using vector databases (RAG)
- Improve citation verification and grounding
- Add streaming responses for better UX
- Build a frontend (Streamlit / React)
- Expand tool ecosystem (news, arXiv, GitHub search)
- Add evaluation metrics for answer quality

---

##  Disclaimer

This project is for **educational purposes only**. It demonstrates experimental patterns in LLM agent design and should not be used as a production-grade factual system without additional validation.

---

##  Summary

This project demonstrates a **self-reflective, tool-augmented AI research agent** built with modern LLM engineering techniques, including:

- Agentic workflows  
- Structured reasoning  
- Tool use integration  
- Iterative refinement loops  
- LangGraph orchestration
