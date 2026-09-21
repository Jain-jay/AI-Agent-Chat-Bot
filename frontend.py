#step 1

import streamlit as st

st.set_page_config(page_title="Langgraph Agent UI", layout="wide")
st.title("AI ChatBot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt=st.text_area("Define you AI Agent: ", height=80 , placeholder="Type your system prompt here....")

MODEL_NAMES_GROQ = ["openai/gpt-oss-120b"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Model Provider: ", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select GROQ Model: ", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model: ", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=169 , placeholder="Ask Anything here....")

API_URL = "http://127.0.0.1:8000/chat"
if st.button("Ask AI Agent"):
    if user_query.strip():
        import requests

        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search,
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if isinstance(response_data, dict) and "error" in response_data:
                st.error(response_data["error"])
            else:
                answer = response_data.get("response", response_data) if isinstance(response_data, dict) else response_data
                st.subheader("AI Agent Response:")
                st.markdown(f"**Final Response:** {answer}")
        else:
            st.error(f"Request failed with status {response.status_code}: {response.text}")
