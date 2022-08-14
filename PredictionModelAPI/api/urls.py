from django.urls import path
from .views import PricePredictionRandomForestRegressor, GetAllRequestedFeatures, GetAllPredictions,GetOnePrediction

urlpatterns = [
    path('price/', PricePredictionRandomForestRegressor.as_view(), name='price_prediction'),
    path('features/', GetAllRequestedFeatures.as_view(), name='all_requested_features'),
    path('predictions/', GetAllPredictions.as_view(), name='all_predictions'),
    path('prediction/<int:pk>/',GetOnePrediction.as_view(),name = 'one_prediction')
]
