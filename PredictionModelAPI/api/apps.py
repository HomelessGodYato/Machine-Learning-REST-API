from django.apps import AppConfig
import os
import pickle, bz2
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "random_forest_regressor_compressed.pkl")
    decompressed = bz2.BZ2File(MODEL_FILE, "rb")
    model = pickle.load(decompressed)
