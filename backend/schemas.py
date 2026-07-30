from pydantic import BaseModel


class PredictionRequest(BaseModel):
    text: str



class PredictionResponse(BaseModel):

    text: str

    category: str

    confidence: float

    classifier: str

    action: str

    priority: str