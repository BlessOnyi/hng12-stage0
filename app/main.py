from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, HttpUrl


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

class DetailResponse(BaseModel):
    email: EmailStr
    current_datetime: str
    github_url: HttpUrl


@app.get("/api/v1/info") 
async def get_details()->DetailResponse:
    data = {
        "email": "onyinyechukwumblessing@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z", 
        "github_url": "https://github.com/BlessOnyi/hng12-stage0.git"
    }
    return data



