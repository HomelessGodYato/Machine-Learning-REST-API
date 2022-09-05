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
from .utils import read_json, save_objects
from django.views.decorators.csrf import csrf_exempt


class GetAllRequestedFeatures(APIView):
    @csrf_exempt
    def get(self, request):
        features = RequestedFeatures.objects.all()
        serializer = RequestedFeaturesSerializer(features, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


class GetAllPredictions(APIView):
    @csrf_exempt
    def get(self, request):
        predictions = PredictedPrice.objects.all()
        serializer = PredictedPriceSerializer(predictions, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


class GetOnePrediction(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            prediction = PredictedPrice.objects.get(pk=pk)
        except PredictedPrice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PredictedPriceSerializer(prediction)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


class PredictFromFile(APIView):
    @csrf_exempt
    def post(self, request, **kwargs):
        serializer = FileSerializer(data=request.FILES)
        if serializer.is_valid():
            serializer.save()
            model = kwargs.get('model')
            returnObject = save_objects(serializer,model)

            return Response(data=returnObject.data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class GetAllFiles(APIView):
    @csrf_exempt
    def get(self, request):
        files = JSONFile.objects.all()
        serializer = FileSerializer(files, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
