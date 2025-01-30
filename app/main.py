from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)



@app.get("/")
async def get_info():
    data = {
        "email": "onyinyechukwumblessing@gmail.com",
        "current_datetime": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",  # Trim to milliseconds
        "github_url": "https://github.com/BlessOnyi/hng12-stage0.git"
    }
    return data