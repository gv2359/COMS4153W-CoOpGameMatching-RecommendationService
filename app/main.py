from fastapi import Depends, FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.routers import recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


app.include_router(recommendations.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Co-Op Game Recommendation Service!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
