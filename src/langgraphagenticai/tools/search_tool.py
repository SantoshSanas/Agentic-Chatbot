from langchain_community.tools.tavily_search import TavilySearchResults
#from langchain_tavily import TavilySearch, TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns a list of tools to be used by the chatbot.
    """
    tools = [TavilySearchResults(max_results=3)]
    return tools

def create_tool_node(tools):
    """
    Creates a ToolNode with the provided tools.
    """
    return ToolNode(tools=tools) 