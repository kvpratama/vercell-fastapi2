from langgraph.graph import MessagesState

class HelloWorldState(MessagesState):
    response: str
