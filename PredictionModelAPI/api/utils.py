import json
from PredictionModelAPI.api.models import RequestedFeatures, PredictedPrice
from PredictionModelAPI.api.serializers import RequestedFeaturesSerializer
from PredictionModelAPI.api.apps import ApiConfig
import numpy as np


def read_json(file):
    data = json.load(open(file.path, "r"))
    predictions = []
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
        predictions.append({"Predicted price": price_predicted})
        feature_serializer = RequestedFeaturesSerializer(features_save)
        feature_id = feature_serializer.data.get('id')
        requested_feature = RequestedFeatures.objects.get(id=feature_id)
        prediction_object = PredictedPrice.objects.create(
            request_id=requested_feature,
            predicted_price=price_predicted
        )
        return predictions
