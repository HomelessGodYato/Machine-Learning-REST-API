import numpy as np
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import RequestedFeatures, PredictedPrice
from .serializers import RequestedFeaturesSerializer, PredictedPriceSerializer
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
        model = ApiConfig.model
        price_predicted = model.predict(input_data)
        price_predicted = np.round(price_predicted, 1)
        feature_serializer = RequestedFeaturesSerializer(features_save)
        feature_id = feature_serializer.data.get('id')
        print(feature_id)
        requested_feature = RequestedFeatures.objects.get(id=feature_id)
        print(requested_feature)
        prediction_object = PredictedPrice.objects.create(
            request_id=requested_feature,
            predicted_price=price_predicted
        )
        print("saved")
        response_dict = {"Predicted Price": price_predicted}
        return Response(response_dict, status=200)


class GetAllRequestedFeatures(APIView):
    def get(self, request):
        features = RequestedFeatures.objects.all()
        serializer = RequestedFeaturesSerializer(features, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


class GetAllPredictions(APIView):
    def get(self, request):
        predictions = PredictedPrice.objects.all()
        serializer = PredictedPriceSerializer(predictions, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


class GetOnePrediction(APIView):
    def get(self, request, pk):
        try:
            prediction = PredictedPrice.objects.get(pk=pk)
        except PredictedPrice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PredictedPriceSerializer(prediction)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
