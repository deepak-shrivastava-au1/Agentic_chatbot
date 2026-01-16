from src.langgraphagenticai.state.state import State
from langchain_core.messages import AIMessage


class BasicChatbotNode:
    """
    Docstring for BasicChatbotNode

    """
    def __init__(self, model):
        self.llm = model
    
    def process(self, state: State)-> dict:
        """
        Process method for BasicChatbotNode

        """
        # Get the messages from state
        messages = state.get('messages', [])
        
        # Invoke the LLM with messages
        response = self.llm.invoke(messages)
        
        # Convert to AIMessage if needed
        if not isinstance(response, AIMessage):
            response = AIMessage(content=str(response))
        
        return {"messages": response} 