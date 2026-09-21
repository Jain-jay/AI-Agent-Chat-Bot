# 🤖 AI-Agent-Chat-Bot

An AI Chatbot application built using **LangGraph**, **FastAPI**, **Streamlit**, **Groq**, **OpenAI**, and **Tavily Web Search**.

## 📁 File Structure
- `ai_agent.py`: Core AI Agent logic with LangGraph, Tavily search, Groq, and OpenAI models.
- `backend.py`: FastAPI server exposing `/chat` endpoint.
- `frontend.py`: Streamlit user interface interacting with the FastAPI backend.

## 🚀 Running Locally

1. **Backend**:
   ```bash
   python backend.py
   ```
2. **Frontend**:
   ```bash
   streamlit run frontend.py
   ```
