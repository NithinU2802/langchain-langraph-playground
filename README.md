# LangChain and Langraph Playground
LangChain is a orchestration framework designed to simplify the creation of app that 
use Large Language Model (LLMs) instead of just treating an LLM as a chatbot it allows developers 
to chain the external data sources, tools and memory to build complex context-aware AI App.

# LangGraph API
    LangGraph provides a Pythonic interface to build and execute agentic workflows using 
graph structures. The API is modular, allowing the practitioner to define nodes, edges and
state transitions with clarity.

LangGraph Core API's - Nodes, Edges, Graph and state

API Components: StateGraph, add_node(), add_edge(), set_entry_point(), set_finish_point(),
compile() and invoke()

A LangGraph Prebuilt Agent is a ready-to-use agentic workflow built using LangGraph's 
graph-based architecture. It combines LLMs, Tools, State management and Routing logic.

> Langgraph agent without LLM

To use langgraph in python install - pip install langgraph