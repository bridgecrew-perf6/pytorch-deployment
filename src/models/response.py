from email import message
from pydantic import BaseModel

class PredictionModel(BaseModel):
    predicted_class: str