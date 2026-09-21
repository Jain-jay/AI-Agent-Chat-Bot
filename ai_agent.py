import os
from dotenv import load_dotenv

# Force load the .env file from the current directory explicitly
base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path=dotenv_path)

def get_api_key(key_name):
    """Retrieve API key from st.secrets or os.environ."""
    try:
        import streamlit as st
        if key_name in st.secrets and st.secrets[key_name]:
            return str(st.secrets[key_name]).strip()
    except Exception:
        pass
    val = os.environ.get(key_name, "")
    return val.strip() if val else ""

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider, custom_api_key=None):
    if provider == "Groq":
        api_key = (custom_api_key.strip() if custom_api_key else "") or get_api_key("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is missing! Please set GROQ_API_KEY in Streamlit Secrets (App Settings -> Secrets) or enter your Groq API Key in the sidebar.")
        os.environ["GROQ_API_KEY"] = api_key
        llm = ChatGroq(model=llm_id, groq_api_key=api_key)
    elif provider == "OpenAI":
        api_key = (custom_api_key.strip() if custom_api_key else "") or get_api_key("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing! Please set OPENAI_API_KEY in Streamlit Secrets (App Settings -> Secrets) or enter your OpenAI API Key in the sidebar.")
        os.environ["OPENAI_API_KEY"] = api_key
        llm = ChatOpenAI(model=llm_id, api_key=api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    if allow_search:
        tavily_key = get_api_key("TAVILY_API_KEY")
        if tavily_key:
            os.environ["TAVILY_API_KEY"] = tavily_key
        tools = [TavilySearchResults(max_results=2)]
    else:
        tools = []
    
    prompt = system_prompt if system_prompt and system_prompt.strip() else "Act as an AI chatbot who is smart and friendly"

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=prompt,
    )

    state = {"messages": query if isinstance(query, list) else [query]}
    response = agent.invoke(state)
    messages = response.get("messages", [])
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    if not ai_messages:
        return "No response generated"
    return ai_messages[-1]



