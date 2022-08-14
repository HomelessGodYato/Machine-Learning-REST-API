import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.preprocessing import StandardScaler


class PricePredictionRandomForestRegressor(APIView):
    def post(self, request):
        data = request.data
        input_data = [data['carat'],
                      data['cut'],
                      data['color'],
                      data['clarity'],
                      data['depth'],
                      data['table'],
                      data['x'],
                      data['y'],
                      data['z']]
        input_data = np.array(input_data).reshape(1, -1)
        # scaler = StandardScaler()
        # scaler.fit(input_data)
        # input_data = scaler.transform(input_data)
        model = ApiConfig.model
        price_predicted = model.predict(input_data)
        price_predicted = np.round(price_predicted, 1)
        response_dict = {"Predicted Price": price_predicted}
        return Response(response_dict, status=200)
