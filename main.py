from fastapi import FastAPI, Request
from pydantic import BaseModel
from utils.generate_video import generate_reel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(request: PromptRequest):
    video_path = generate_reel(request.prompt)
    return {"status": "success", "video_url": f"/videos/{video_path}"}