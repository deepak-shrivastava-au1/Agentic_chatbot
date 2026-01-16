import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json


class DisplayResultStreamlitUI:
    def __init__(self, usecase: str, graph=None, user_message: str = ""):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        """Display the result in the Streamlit UI."""
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_message)
        
        # Stream response from graph
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            try:
                for event in graph.stream({"messages": [HumanMessage(content=user_message)]}):
                    for value in event.values():
                        if "messages" in value:
                            message = value["messages"]
                            # Extract content from the message
                            if hasattr(message, 'content'):
                                full_response = message.content
                            else:
                                full_response = str(message)
                
                response_placeholder.write(full_response)
            except Exception as e:
                st.error(f"Error processing response: {e}")
