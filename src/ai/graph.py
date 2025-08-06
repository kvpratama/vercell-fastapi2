from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from .state import HelloWorldState

# Replace with your actual Google API key or ensure it's set in your environment
import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY_HERE")

llm = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY,
    model="gemini-2.5-flash-lite"
)

def hello_node(state: HelloWorldState) -> HelloWorldState:
    # Use the LLM to generate a hello world message
    response = llm.invoke("Say hello world with current time.")
    return {"response": response}

# Build the graph
workflow = StateGraph(HelloWorldState)
workflow.add_node("hello", hello_node)
workflow.set_entry_point("hello")
workflow.add_edge("hello", END)
workflow_app = workflow.compile()

if __name__ == "__main__":
    final_state = app.invoke({"messages": []})
    print(final_state["response"].content)
