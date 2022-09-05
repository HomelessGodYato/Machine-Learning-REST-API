from django.apps import AppConfig
import os
import joblib
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    models = {
                "RandomForestRegressor":joblib.load(os.path.join(settings.MODELS, "RandomForestRegressor.pkl")),
                "KNeighborsRegressor":joblib.load(os.path.join(settings.MODELS, "KNeighborsRegressor.pkl"))
             }

    scores = {
                "RandomForestRegressor":joblib.load(os.path.join(settings.SCORES, "RandomForestRegressor_score.pkl")),
                "KNeighborsRegressor":joblib.load(os.path.join(settings.SCORES, "KNeighborsRegressor_score.pkl"))
             }
    
    encoders = {
                 "ColorEncoder": joblib.load(os.path.join(settings.ENCODERS, "color_encoder.pkl")),
                 "CutEncoder":joblib.load(os.path.join(settings.ENCODERS, "cut_encoder.pkl")),
                 "ClarityEncoder":joblib.load(os.path.join(settings.ENCODERS, "clarity_encoder.pkl"))
               }

