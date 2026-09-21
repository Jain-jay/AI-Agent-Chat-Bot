#step 1 
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

#step2
from fastapi import FastAPI

ALLOWED_MODEL_NAMES = ["gpt-4o-mini", "openai/gpt-oss-120b"]

app = FastAPI(title="Langgraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the ChatBot using Langgraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name, Kindly select a valid AI model"}

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    response = get_response_from_ai_agent(
        llm_id,
        query,
        allow_search,
        system_prompt,
        provider,
    )
    return {"response": response}

#step3 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)