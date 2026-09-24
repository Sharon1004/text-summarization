from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel, Field, field_validator


from backend.summarizer import summarize_text

app=FastAPI()

class SummarizeRequest(BaseModel):
    text: str
    summary_length: int = Field(ge=1, le=10)

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty")
        return value
@app.get("/")
def home():
    return {"message":"Text Summarization API is running"}

@app.post("/summarize")
def summarize(request:SummarizeRequest):
    summary=summarize_text(request.text,request.summary_length)
    return {"summary":summary}
