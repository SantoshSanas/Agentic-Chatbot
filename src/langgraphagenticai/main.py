import streamlit as st

from src.langgraphagenticai.ui.streamlitui.display_results import DisplayResultStreamlit
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder

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
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message to the Agentic AI:")

    if user_message:
        try:
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM model. Please check your configuration.")
                return
            ## Initialize and set up the graph based on use case
            usecases = user_input.get("selected_usecase")

            if not usecases:
                st.error("No use case selected. Please select a use case from the sidebar.")
                return
            
            ## Graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase=usecases)
                DisplayResultStreamlit(usecase=usecases, graph=graph, user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up the graph: {e}")
                return

        except Exception as e:
            st.error(f"An error occurred: {e}")
            return