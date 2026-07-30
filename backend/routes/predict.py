from fastapi import APIRouter

from backend.schemas import (
    PredictionRequest,
    PredictionResponse
)

from backend.services.prediction_service import (
    predict_signal
)



router = APIRouter()



@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
    request: PredictionRequest
):

    result = predict_signal(
        request.text
    )

    return result