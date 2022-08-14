import json
from .models import RequestedFeatures, PredictedPrice
from .serializers import RequestedFeaturesSerializer
from .apps import ApiConfig
import numpy as np


def read_json(file):
    data = json.load(open(file.path, "r"))
    return data
