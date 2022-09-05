from django.urls import path
from .views import \
    GetAllRequestedFeatures, \
    GetAllPredictions, \
    GetOnePrediction, \
    PredictFromFile, \
    GetAllFiles

from .apps import ApiConfig

urlpatterns = [
    path('api/features/', GetAllRequestedFeatures.as_view(), name='all_requested_features'),
    path('api/predictions/', GetAllPredictions.as_view(), name='all_predictions'),
    path('api/prediction/<int:pk>/', GetOnePrediction.as_view(), name='one_prediction'),
    path('api/files/get_all/', GetAllFiles.as_view(), name='get_all_files'),
    
    path('api/rf_regressor/json/upload/', PredictFromFile.as_view(),{'model':ApiConfig.models['RandomForestRegressor']}, name='predict_from_file'),
    path('api/knn_regressor/json/upload/', PredictFromFile.as_view(),{'model':ApiConfig.models['KNeighborsRegressor']}, name='predict_from_file_knn'),

]
