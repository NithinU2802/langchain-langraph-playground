from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END
from typing import TypedDict
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get model name from .env
model_name = os.getenv("MODEL_NAME")

# Initialize LLM model
chat_model = ChatOllama(model=model_name)

# Define the state
class ChatState(TypedDict):
    chat_history: list
    generated_response: str

# Function to generate response from the model
def generate_response(state: ChatState) -> ChatState:
    chat_history = state["chat_history"]
    model_output = chat_model.invoke(chat_history)
    
    return {"generated_response": model_output.content}

# Create then config the graph
conversation_graph = StateGraph(ChatState)
conversation_graph.add_node("response_generator", generate_response)
conversation_graph.set_entry_point("response_generator")
conversation_graph.add_edge("response_generator", END)

# Compile the graph
chat_app = conversation_graph.compile()

# Initial input
initial_input = {"chat_history": [("user", "Hi, What can you do?")]}

# Invoke the app
final_result = chat_app.invoke(initial_input)

# Print the response
print(final_result["generated_response"])