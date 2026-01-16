from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from langgraph.graph import StateGraph, START, END

class GraphBuilder:
    def __init__(self, model, usecase: str = None, user_message: str = None):
        """Initialize GraphBuilder with the LLM model and optional context."""
        self.llm = model
        self.usecase = usecase
        self.user_message = user_message
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """Builds the chatbot graph using the provided LLM model."""
        
        chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        """Sets up the graph based on the selected use case."""
        
        if usecase == "Chatbot with tools":
            self.basic_chatbot_build_graph()
        else:
            # Default to basic chatbot for any usecase
            self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()