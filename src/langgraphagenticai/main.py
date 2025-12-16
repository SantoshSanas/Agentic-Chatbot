import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agentic_ai_app():
    """
    Load the LangGraph Agentic AI application.
    This function initializes the Streamlit UI and returns user controls, sets up the page configuration, and handles user inputs.
    and displays the application interface.
    """
    ui_loader = LoadStreamlitUI()
    user_input = ui_loader.load_streamlit_ui()

    if not user_input:
        st.error("No user input received. Please make selections in the sidebar.")
        return
    
    user_message = st.chat_input("Enter your message to the Agentic AI:")

    