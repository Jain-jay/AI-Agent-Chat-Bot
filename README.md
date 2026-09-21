# 🤖 LangGraph AI Agent ChatBot

An intelligent, multi-provider AI Agent ChatBot built using **LangGraph**, **FastAPI**, **Streamlit**, **Groq**, **OpenAI**, and **Tavily Web Search**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)
![LangChain](https://img.shields.io/badge/LangChain-LangGraph-green.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

---

## 📌 Table of Contents
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Environment Setup](#-environment-setup)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [License](#-license)

---

## ✨ Features

- 🧠 **Dual AI Provider Support**: Seamlessly switch between **Groq** (`openai/gpt-oss-120b`) and **OpenAI** (`gpt-4o-mini`).
- 🌐 **Real-time Web Search**: Integrated with **Tavily Search API** via LangChain tools to fetch up-to-date web search results.
- 🎯 **Custom System Prompts**: Define tailored personalities and behavior for your AI Agent directly from the UI.
- ⚡ **Fast API Backend**: Clean decoupled REST API built with **FastAPI** & Pydantic request validation.
- 💻 **Interactive UI**: User-friendly frontend powered by **Streamlit**.

---

## 🏗️ Architecture

```text
┌─────────────────┐        HTTP POST        ┌─────────────────┐
│                 │  http://127.0.0.1:8000  │                 │
│  Streamlit UI   │ ──────────────────────> │ FastAPI Backend │
│  (frontend.py)  │                         │  (backend.py)   │
└─────────────────┘                         └────────┬────────┘
                                                     │
                                                     ▼
                                            ┌─────────────────┐
                                            │ LangGraph Agent │
                                            │  (ai_agent.py)  │
                                            └────────┬────────┘
                                                     │
                             ┌───────────────────────┴───────────────────────┐
                             ▼                                               ▼
                  ┌────────────────────┐                           ┌──────────────────┐
                  │ Groq / OpenAI LLM  │                           │  Tavily Search   │
                  └────────────────────┘                           └──────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Description |
|---|---|---|
| **Frontend** | [Streamlit](https://streamlit.io) | Interactive Web UI |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com) | REST API framework |
| **Orchestration**| [LangGraph](https://python.langchain.com) / LangChain | ReAct Agent workflow framework |
| **LLMs** | [Groq](https://groq.com) / [OpenAI](https://openai.com) | AI Inference Engine |
| **Search Engine**| [Tavily AI](https://tavily.com) | Web Search API for AI Agents |

---

## 🔑 Prerequisites & Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jain-jay/AI-Agent-Chat-Bot.git
   cd AI-Agent-Chat-Bot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Linux/macOS
   # .venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn streamlit langchain langchain-groq langchain-openai langchain-community langgraph tavily-python python-dotenv pydantic requests
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

---

## 🚀 Getting Started

### Step 1: Start the FastAPI Backend
Launch the backend server on `http://127.0.0.1:8000`:
```bash
python backend.py
```

### Step 2: Start the Streamlit Frontend
In a new terminal window or tab, run:
```bash
streamlit run frontend.py
```

Open your browser at `http://localhost:8501` to interact with your AI Agent!

---

## 📡 API Reference

### POST `/chat`

Interact with the AI Agent via API.

**Request Body (`JSON`):**
```json
{
  "model_provider": "Groq",
  "model_name": "openai/gpt-oss-120b",
  "system_prompt": "You are a helpful coding assistant.",
  "messages": ["Explain quantum computing in simple terms."],
  "allow_search": true
}
```

**Response Body (`JSON`):**
```json
{
  "response": "Quantum computing is a type of computing that uses..."
}
```

---

## 📜 License

Distributed under the MIT License.
