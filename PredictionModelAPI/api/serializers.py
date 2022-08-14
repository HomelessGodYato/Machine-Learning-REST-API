from rest_framework import serializers
from .models import RequestedFeatures, PredictedPrice


class RequestedFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedFeatures

        fields = "__all__"
