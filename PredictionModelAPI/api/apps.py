from django.apps import AppConfig
import os
import pickle, bz2,joblib
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "random_forest_regressor.pkl")
    COLOR_ENCODER_FILE = os.path.join(settings.ENCODERS, "color_encoder.pkl")
    CUT_ENCODER_FILE = os.path.join(settings.ENCODERS, "cut_encoder.pkl")
    CLARITY_ENCODER_FILE = os.path.join(settings.ENCODERS, "clarity_encoder.pkl")

    model = joblib.load(MODEL_FILE)
    color_enc = joblib.load(COLOR_ENCODER_FILE)
    cut_enc = joblib.load(CUT_ENCODER_FILE)
    clarity_enc = joblib.load(CLARITY_ENCODER_FILE)
