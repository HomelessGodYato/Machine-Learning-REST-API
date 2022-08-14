import numpy as np
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import RequestedFeatures
from .serializers import RequestedFeaturesSerializer
from django.http import JsonResponse



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

        features_save = RequestedFeatures.objects.create(
            carat=input_data[0],
            cut=ApiConfig.cut_enc.inverse_transform(np.array([input_data[1]])),
            color=ApiConfig.color_enc.inverse_transform(np.array([input_data[2]])),
            clarity=ApiConfig.clarity_enc.inverse_transform(np.array([input_data[3]])),
            depth=input_data[4],
            table=input_data[5],
            x=input_data[6],
            y=input_data[7],
            z=input_data[8]
        )

        input_data = np.array(input_data).reshape(1, -1)
        # scaler = StandardScaler()
        # scaler.fit(input_data)
        # input_data = scaler.transform(input_data)
        model = ApiConfig.model
        price_predicted = model.predict(input_data)
        price_predicted = np.round(price_predicted, 1)
        response_dict = {"Predicted Price": price_predicted}
        return Response(response_dict, status=200)


class GetAllRequestedFeatures(APIView):
    def get(self, request):
        features = RequestedFeatures.objects.all()
        serializer = RequestedFeaturesSerializer(features, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
