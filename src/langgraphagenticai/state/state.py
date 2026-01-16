from typing_extensions import TypedDict, List
from langgraph.graph import add_messages
from typing import Annotated


class State(TypedDict):
    """State representation for the LangGraph AgenticAI application."""
    messages: Annotated[List, add_messages]