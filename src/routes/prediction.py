from fastapi import APIRouter, File, Request

from src.models.response import PredictionModel

router = APIRouter()

@router.post("/predict", response_model=PredictionModel)
def predict(request: Request, file: bytes = File(...)):
    """Performs image classification prediction based on imagenet
    """
    class_label = request.app.state.model.predict(file)
    return PredictionModel(predicted_class=class_label)