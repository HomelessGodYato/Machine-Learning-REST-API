from django.urls import path
from .views import \
    GetAllRequestedFeatures, \
    GetAllPredictions, \
    GetOnePrediction, \
    PredictFromFile, \
    GetAllFiles

urlpatterns = [
    path('api/rf_cls/features/', GetAllRequestedFeatures.as_view(), name='all_requested_features'),
    path('api/rf_cls/predictions/', GetAllPredictions.as_view(), name='all_predictions'),
    path('api/rf_cls/prediction/<int:pk>/', GetOnePrediction.as_view(), name='one_prediction'),
    path('api/rf_cls/json/upload/', PredictFromFile.as_view(), name='predict_from_file'),
    path('api/rf_cls/files/get_all/',GetAllFiles.as_view(),name = 'get_all_files')

]
