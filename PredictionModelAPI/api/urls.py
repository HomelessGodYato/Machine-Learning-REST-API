from django.urls import path
from .views import PricePredictionRandomForestRegressor

urlpatterns = [
    path('price/', PricePredictionRandomForestRegressor.as_view(), name = 'price_prediction'),
]