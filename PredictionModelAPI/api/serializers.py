from rest_framework import serializers
from .models import RequestedFeatures, PredictedPrice


class RequestedFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedFeatures

        fields = "__all__"


class PredictedPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictedPrice

        fields = "__all__"
