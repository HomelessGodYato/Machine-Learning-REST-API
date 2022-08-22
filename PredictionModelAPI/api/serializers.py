from rest_framework import serializers
from .models import RequestedFeatures, PredictedPrice, JSONFile, MLModel


class PredictedPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictedPrice

        fields = "__all__"


class RequestedFeaturesSerializer(serializers.ModelSerializer):
    prediction = PredictedPriceSerializer(many=True, read_only=True)

    class Meta:
        model = RequestedFeatures

        fields = ["id",
                  "carat",
                  "cut",
                  "color",
                  "clarity",
                  "depth",
                  "table",
                  "x",
                  "y",
                  "z",
                  "prediction"]


class MLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = ["model_name",
                  "model_score"]


class FileSerializer(serializers.ModelSerializer):
    ml_model = MLModelSerializer(many=True, read_only=True)
    features = RequestedFeaturesSerializer(many=True, read_only=True)

    class Meta:
        model = JSONFile
        fields = ["id",
                  "file",
                  "created",
                  "ml_model",
                  "features"]
