import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            # Accept key from the sidebar first, then fall back to environment
            groq_api_key = (self.user_controls_input.get("GROQ_API_KEY") or
                            os.environ.get("GROQ_API_KEY", ""))
            selected_groq_model = self.user_controls_input.get("selected_groq_model", "")

            if not groq_api_key:
                raise ValueError("GROQ API Key is missing. Please set it in the sidebar or as the GROQ_API_KEY environment variable.")
            if not selected_groq_model:
                raise ValueError("Groq model not selected. Please choose a model from the sidebar.")

            llm = ChatGroq(
                api_key=groq_api_key,
                model=selected_groq_model
            )

        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")
        
        return llm

