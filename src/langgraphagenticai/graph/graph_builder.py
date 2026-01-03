from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import START, END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraphagenticai.nodes.chatbot_with_websearch_tool_node import ChatbotWebsearchToolNode
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using the provided LLM.
        This method initializes the StateGraph with the given LLM model.
        and integrates it into the graph structure. The chatbot node i set as both the
        start and end node of the graph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def chatbot_with_tools_build_graph(self):
        """
        Builds a chatbot with tools graph using the provided LLM.
        This method initializes the StateGraph with the given LLM model
        and integrates tool-using capabilities into the graph structure.
        The chatbot node is set as both the start and end node of the graph.
        """
        # Placeholder for future implementation
        tools = get_tools()
        tool_node = create_tool_node(tools)

        ## Define LLM
        llm = self.llm
        ## Define Chatbot Node with Tools
        obj_chatbot_with_node = ChatbotWebsearchToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        ## Add Nodes
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        ## Add Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def ai_news_builder_graph(self):

        ai_news_node = AINewsNode(self.llm)

        ## Add Nodes
        self.graph_builder.add_node("fetch_news", ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news", ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result", ai_news_node.save_result)

        ## Add Edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result",END)


    def setup_graph(self, usecase:str):
        """
        sets up the graph for the specified use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Web Search":
            self.chatbot_with_tools_build_graph()
        if usecase == "AI News":
            self.ai_news_builder_graph()

        return self.graph_builder.compile()