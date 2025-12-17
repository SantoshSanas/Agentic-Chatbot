from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    logic implementation for a basic chatbot node within a StateGraph.
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state:State) -> dict:
        """
        process method to handle incoming messages and generate responses using the LLM.
        """
        return {"messages":self.llm.invoke(state["message"])}