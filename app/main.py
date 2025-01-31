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



@app.get("/api/v1/info")
async def get_details():
    data = {
        "email": "onyinyechukwumblessing@gmail.com",
        "current_datetime": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z", 
        "github_url": "https://github.com/BlessOnyi/hng12-stage0.git"
    }
    return data