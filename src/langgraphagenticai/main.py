import streamlit as st
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlitUI
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamliUI
from src.langgraphagenticai.ui.uiconfigfile import Config
from src.langgraphagenticai.LLMs.groqllm import GroqLLM

def load_langgraph_agenticai_app():
    """Load the LangGraph AgenticAI Streamlit application."""

    ## Load UI
    ui_loader = LoadStreamliUI()
    user_controls = ui_loader.load_streamlit_ui()

    if not user_controls:
        st.error("Error : Please select configuration options from the sidebar.")
        return
    
    user_message = st.chat_input("Enter your message:")
    if user_message:
        try:
            ## Configure and run the agentic AI based on user controls
            
            obj_llm_config = GroqLLM(user_controls_input=user_controls)
            model = obj_llm_config.get_llm_model()

            if model is None:
                st.error("Error: LLM model could not be initialized. Please check your configuration.")
                return

            ## Initialize and run the agentic AI with the selected model and user message
            usecase = user_controls.get('selected_usecase', 'Chatbot with tools')

            if not usecase:
                st.error("Error: Please select a valid use case.")
                return
            
            ## Graph Builder

            graph_builder = GraphBuilder(model=model, usecase=usecase, user_message=user_message)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlitUI(usecase=usecase, graph=graph, user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error in setting up the graph: {e}")
                return
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return