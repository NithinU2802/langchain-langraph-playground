# LangGraph Agent without LLM

from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class ResearchState(TypedDict):
    user_query: str
    research_data: str
    summarized_text: str
    review_notes: str
    final_report: str


def research_agent(state: ResearchState):
    query = state["user_query"]
    result = f"Web research collected for: {query}"
    return {"research_data": result}


def summarizer_agent(state: ResearchState):
    data = state["research_data"]
    summary = f"Summary created from research: {data}"
    return {"summarized_text": summary}


def critique_agent(state: ResearchState):
    summary = state["summarized_text"]
    critique = f"Review and critique of summary: {summary}"
    return {"review_notes": critique}


def presenter_agent(state: ResearchState):
    notes = state["review_notes"]
    report = f"Final formatted report:\n{notes}"
    return {"final_report": report}


builder = StateGraph(ResearchState)

builder.add_node("research_agent", research_agent)
builder.add_node("summarizer_agent", summarizer_agent)
builder.add_node("critique_agent", critique_agent)
builder.add_node("presenter_agent", presenter_agent)


builder.add_edge(START, "research_agent")
builder.add_edge("research_agent", "summarizer_agent")
builder.add_edge("summarizer_agent", "critique_agent")
builder.add_edge("critique_agent", "presenter_agent")
builder.add_edge("presenter_agent", END)


workflow = builder.compile()


result = workflow.invoke(
    {"user_query": "What are the latest AI trends in India?"}
)

print(result["final_report"])
