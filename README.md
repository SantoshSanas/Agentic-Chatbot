# AgenticChatbot — LangGraph-based Stateful Chatbot

A minimal demo that builds a stateful chatbot using LangGraph and a Groq-backed LLM via Streamlit UI.

## Quick start

1. Create / activate a Python environment (recommended: conda or venv).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   # or: python app.py
   ```

4. In the sidebar: select **LLM = Groq**, choose a **Groq model**, and enter your **GROQ API Key** (or set `GROQ_API_KEY` env var). Select **Use Case** — either **Basic Chatbot** or **Chatbot with Web Search**. If you choose **Chatbot with Web Search**, a field to enter your **TAVILY API Key** will appear (or set `TAVILY_API_KEY` env var) to enable web search tools.
5. Type a message (e.g., "Hi") in the chat input and send.

## Required configuration

- A valid GROQ API key (sidebar or env var `GROQ_API_KEY`) and a supported Groq model.
- (Optional) If using **Chatbot with Web Search**, provide a **TAVILY API Key** via the sidebar or set the `TAVILY_API_KEY` environment variable; the search tool depends on the Tavily service (see `requirements.txt`).

## Project structure (key files)

- `app.py` — entry point that starts the Streamlit app.
- `src/langgraphagenticai/main.py` — builds UI and handles user interactions.
- `src/langgraphagenticai/LLMs/groqllm.py` — initializes Groq LLM client.
- `src/langgraphagenticai/graph/graph_builder.py` — constructs the LangGraph workflow.
- `src/langgraphagenticai/nodes/basic_chatbot_node.py` — node that calls the LLM.
- `src/langgraphagenticai/tools/search_tool.py` — web search tool (Tavily) used by the **Chatbot with Web Search** use case.
- `src/langgraphagenticai/ui/streamlitui/` — UI components (`loadui.py`, `display_results.py`).
- `src/langgraphagenticai/ui/uiconfigfile.ini` — UI defaults (page title, use cases, model options).

## Troubleshooting

- If no response appears, check:
  - GROQ key and model are set in the sidebar (or `GROQ_API_KEY` env var). 
  - Use Case is set correctly (e.g., **Basic Chatbot** or **Chatbot with Web Search**); if using web search, make sure **TAVILY_API_KEY** is provided in the sidebar or as an environment variable.
  - Streamlit logs for any `st.error` messages shown in the UI or terminal.

## License

MIT-style (refer to project root if present).
