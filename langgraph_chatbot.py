import os
import getpass

# ---- Set LangSmith API Key ----
if not os.environ.get("LANGSMITH_API_KEY"):
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API Key: ")

# Enable tracing
os.environ["LANGSMITH_TRACING"] = "true"


# ---- Import Libraries ----
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


# ---- Define LLM Model ----
huggingface_model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=128,
    temperature=0.1,
)

chat_model = ChatHuggingFace(llm=huggingface_model)


# ---- Define Graph State ----
class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


# ---- Build Graph ----
graph_builder = StateGraph(ChatState)


# ---- Chatbot Node ----
def chatbot_node(state: ChatState):
    response = chat_model.invoke(state["messages"])
    return {"messages": [response]}


# ---- Add Node and Edges ----
graph_builder.add_node("chatbot", chatbot_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


# ---- Compile Graph ----
chat_graph = graph_builder.compile()


# ---- Chat Loop ----
while True:
    user_input = input("User: ")

    if user_input.lower() in ["quit", "q", "exit"]:
        print("Thank you! Bye")
        break

    for event in chat_graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("AI Model:", value["messages"][-1].content)