# 🤖 AI-Agent-Chat-Bot

An intelligent AI Chatbot application built using **LangGraph**, **Streamlit**, **Groq**, **OpenAI**, and **Tavily Web Search**.

## 🌟 Features
- 🚀 **Multiple Model Providers**: Choose between **Groq** (`openai/gpt-oss-120b`) and **OpenAI** (`gpt-4o-mini`).
- 🌐 **Web Search Integration**: Toggle real-time Tavily search for fetching up-to-date information.
- ⚙️ **Custom System Prompts**: Define custom behavior for your AI Agent.
- 💬 **Interactive Chat UI**: Persistent chat history powered by Streamlit's native chat components.

## 🛠️ Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Jain-jay/AI-Agent-Chat-Bot.git
   cd AI-Agent-Chat-Bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

4. **Run the App**:
   ```bash
   streamlit run streamlit_app.py
   ```

## ☁️ Deployment on Streamlit Community Cloud
1. Fork / Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Connect your repository and set `streamlit_app.py` as the main entry point.
4. Add your API keys (`GROQ_API_KEY`, `OPENAI_API_KEY`, `TAVILY_API_KEY`) under **App Settings -> Secrets**.
5. Click **Deploy**!
