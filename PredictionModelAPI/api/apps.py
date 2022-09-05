from django.apps import AppConfig
import os
import joblib
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    RF_MODEL_FILE = os.path.join(settings.MODELS, "random_forest_regressor.pkl")

    RF_SCORE_FILE = os.path.join(settings.SCORES, "rfc_score.pkl")
    
    COLOR_ENCODER_FILE = os.path.join(settings.ENCODERS, "color_encoder.pkl")
    CUT_ENCODER_FILE = os.path.join(settings.ENCODERS, "cut_encoder.pkl")
    CLARITY_ENCODER_FILE = os.path.join(settings.ENCODERS, "clarity_encoder.pkl")

    rf_model = joblib.load(RF_MODEL_FILE)

    models = {
                "RandomForestRegressor":joblib.load(os.path.join(settings.MODELS, "random_forest_regressor.pkl"))
             }

    scores = {
                "RandomForestScore":joblib.load(os.path.join(settings.SCORES, "rfc_score.pkl"))
             }
    
    encoders = {
                    "ColorEncoder": joblib.load(os.path.join(settings.ENCODERS, "color_encoder.pkl")),
               }
    rf_score = joblib.load(RF_SCORE_FILE)

    color_enc = joblib.load(COLOR_ENCODER_FILE)
    cut_enc = joblib.load(CUT_ENCODER_FILE)
    clarity_enc = joblib.load(CLARITY_ENCODER_FILE)
