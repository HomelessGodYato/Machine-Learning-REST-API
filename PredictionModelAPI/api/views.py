import json
import numpy as np
import os
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RequestedFeatures, PredictedPrice, JSONFile
from .serializers import RequestedFeaturesSerializer, PredictedPriceSerializer, FileSerializer
from django.http import JsonResponse
from .utils import read_json


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


class PredictFromFile(APIView):
    def post(self, request):
        serializer = FileSerializer(data=request.FILES)
        if serializer.is_valid():
            serializer.save()

            fileId = serializer.data.get('id')
            fileObject = JSONFile.objects.get(id=fileId)

            data = read_json(fileObject.file)
            predictions = []
            model = ApiConfig.model

            for i in range(len(data)):
                data_from_json = {k: v for k, v in data[i].items()}

                input_data = [data_from_json['carat'],
                              data_from_json['cut'],
                              data_from_json['color'],
                              data_from_json['clarity'],
                              data_from_json['depth'],
                              data_from_json['table'],
                              data_from_json['x'],
                              data_from_json['y'],
                              data_from_json['z']]

                input_data = np.array(input_data).reshape(1, -1)
                print(input_data)
                price_predicted = model.predict(input_data)
                price_predicted = np.round(price_predicted, 1)
                predictions.append({"Predicted price": price_predicted})

                features_object = RequestedFeatures.objects.create(
                    file_id=fileObject,
                    carat=input_data[0][0],
                    cut=ApiConfig.cut_enc.inverse_transform([input_data[0][1].astype(int)]),
                    color=ApiConfig.color_enc.inverse_transform([input_data[0][2].astype(int)]),
                    clarity=ApiConfig.clarity_enc.inverse_transform([input_data[0][3].astype(int)]),
                    depth=input_data[0][4],
                    table=input_data[0][5],
                    x=input_data[0][6],
                    y=input_data[0][7],
                    z=input_data[0][8]
                )
                PredictedPrice.objects.create(
                    features_id=features_object,
                    predicted_price=price_predicted
                )

                returnObject = FileSerializer(instance=fileObject)
            return Response(data=returnObject.data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class GetAllFiles(APIView):
    def get(self, request):
        files = JSONFile.objects.all()
        serializer = FileSerializer(files, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)