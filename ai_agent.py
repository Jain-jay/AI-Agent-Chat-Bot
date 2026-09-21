import os
from dotenv import load_dotenv

# Force load the .env file from the current directory explicitly
base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path=dotenv_path)

# Sync st.secrets into os.environ for Streamlit Cloud deployment
try:
    import streamlit as st
    for key in ["GROQ_API_KEY", "OPENAI_API_KEY", "TAVILY_API_KEY"]:
        if key in st.secrets and not os.environ.get(key):
            os.environ[key] = str(st.secrets[key])
except Exception:
    pass

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    
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


