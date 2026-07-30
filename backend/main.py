from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.predict import router


app = FastAPI(
    title="Signal Triage AI",
    description="AI powered signal classification system",
    version="1.0"
)


# Enable React frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Prediction routes
app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Signal Triage AI API running"
    }