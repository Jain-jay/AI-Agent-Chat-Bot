import streamlit as st
from ai_agent import get_response_from_ai_agent

st.set_page_config(page_title="AI Agent ChatBot", page_icon="🤖", layout="wide")

st.title("🤖 AI ChatBot Agents")
st.caption("Interact with intelligent AI agents powered by LangGraph, Groq, OpenAI & Tavily Search")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Agent Settings")
    
    provider = st.radio("Select Model Provider:", ["Groq", "OpenAI"])
    
    MODEL_NAMES_GROQ = ["openai/gpt-oss-120b"]
    MODEL_NAMES_OPENAI = ["gpt-4o-mini"]
    
    if provider == "Groq":
        selected_model = st.selectbox("Select GROQ Model:", MODEL_NAMES_GROQ)
    else:
        selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)
        
    allow_web_search = st.checkbox("Allow Web Search (Tavily)", value=False)
    
    system_prompt = st.text_area(
        "Define AI Agent System Prompt:",
        height=100,
        placeholder="e.g. Act as a helpful expert assistant...",
        value="Act as an AI chatbot who is smart and friendly"
    )
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask anything..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Agent is thinking..."):
            try:
                response_text = get_response_from_ai_agent(
                    llm_id=selected_model,
                    query=[prompt],
                    allow_search=allow_web_search,
                    system_prompt=system_prompt,
                    provider=provider,
                )
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
