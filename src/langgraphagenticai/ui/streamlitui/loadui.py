import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamliUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            st.subheader("Configuration Options")

            llm_options = self.config.get_llm_options()
            selected_llm = st.selectbox("Select LLM Model:", llm_options)
            self.user_controls['selected_llm'] = selected_llm

            if self.user_controls['selected_llm'].strip().upper() == "GROQ":
                groq_model_options = self.config.get_groq_model_options()
                selected_groq_model = st.selectbox("Select GROQ Model:", groq_model_options)
                self.user_controls['selected_groq_model'] = selected_groq_model
                # Create the input first using a consistent key, then read it safely
                st.text_input("API Key:", type="password", key="GROQ_API_KEY")
                # Use .get to avoid KeyError if the key isn't in session_state yet
                self.user_controls['GROQ_API_KEY'] = st.session_state.get('GROQ_API_KEY')

    ## Use Case Selection
            usecase_options = self.config.get_usecase_options()
            selected_usecase = st.selectbox("Select Use Case:", usecase_options)
            self.user_controls['selected_usecase'] = selected_usecase

        return self.user_controls

