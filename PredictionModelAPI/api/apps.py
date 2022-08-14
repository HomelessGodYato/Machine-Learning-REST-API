from django.apps import AppConfig
import os
import pickle, bz2
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "random_forest_regressor_compressed.pkl")
    COLOR_ENCODER_FILE = os.path.join(settings.ENCODERS, "color_encoder.pkl")
    CUT_ENCODER_FILE = os.path.join(settings.ENCODERS, "cut_encoder.pkl")
    CLARITY_ENCODER_FILE = os.path.join(settings.ENCODERS, "clarity_encoder.pkl")

    decompressed = bz2.BZ2File(MODEL_FILE, "rb")

    model = pickle.load(decompressed)
    color_enc = pickle.load(open(COLOR_ENCODER_FILE, "rb"))
    cut_enc = pickle.load(open(CUT_ENCODER_FILE, "rb"))
    clarity_enc = pickle.load(open(CLARITY_ENCODER_FILE, "rb"))
