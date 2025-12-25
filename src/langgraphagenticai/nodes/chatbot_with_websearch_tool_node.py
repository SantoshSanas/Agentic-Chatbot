from src.langgraphagenticai.state.state import State


class ChatbotWebsearchToolNode:
    """
    logic implementation for a chatbot with web search node within a StateGraph.
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state:State) -> dict:
        """
        process method to handle incoming messages and generate responses using the LLM with tool integration.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content":user_input}])
        # Here, you would typically integrate the web search tool logic.
        tools_response = f"Tool integrated response to: '{user_input}' "
        return {"messages":[llm_response,tools_response]}
    
    def create_chatbot(self, tools):
        """
        Returns a chatbot function that processes messages using the LLM and tools.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing messages with web search tool integration and returning response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        return chatbot_node