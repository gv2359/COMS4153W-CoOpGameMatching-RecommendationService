from fastapi import Depends, FastAPI
import uvicorn
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from app.routers import recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# it loads from the .env file
load_dotenv()

app.include_router(recommendations.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Co-Op Game Recommendation Service!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)
