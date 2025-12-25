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

4. In the sidebar: select **LLM = Groq**, choose a **Groq model**, and enter your **GROQ API Key** (or set `GROQ_API_KEY` env var). Select **Use Case = Basic Chatbot**.
5. Type a message (e.g., "Hi") in the chat input and send.

## Required configuration

- A valid GROQ API key (sidebar or env var `GROQ_API_KEY`) and a supported Groq model.

## Project structure (key files)

- `app.py` — entry point that starts the Streamlit app.
- `src/langgraphagenticai/main.py` — builds UI and handles user interactions.
- `src/langgraphagenticai/LLMs/groqllm.py` — initializes Groq LLM client.
- `src/langgraphagenticai/graph/graph_builder.py` — constructs the LangGraph workflow.
- `src/langgraphagenticai/nodes/basic_chatbot_node.py` — node that calls the LLM.
- `src/langgraphagenticai/ui/streamlitui/` — UI components (`loadui.py`, `display_results.py`).
- `src/langgraphagenticai/ui/uiconfigfile.ini` — UI defaults (page title, use cases, model options).

## Troubleshooting

- If no response appears, check:
  - GROQ key and model are set in the sidebar (or `GROQ_API_KEY` env var). 
  - Use Case is set to **Basic Chatbot**.
  - Streamlit logs for any `st.error` messages shown in the UI or terminal.

## License

MIT-style (refer to project root if present).
