from fastapi import FastAPI

from src.artifacts.metadata import metadata
from src.predictors.predictor import Predictor
from src.routes import prediction



def create_app():
    app = FastAPI(**metadata)
    app.state.model = Predictor()
    app.include_router(prediction.router)

    return app
