import json
from .models import RequestedFeatures, PredictedPrice, JSONFile, MLModel
from .serializers import FileSerializer
from .apps import ApiConfig
import numpy as np


def read_json(file):
    data = json.load(open(file.path, "r"))
    return data


def save_objects(serializer):
    fileId = serializer.data.get('id')
    file_object = JSONFile.objects.get(id=fileId)

    data = read_json(file_object.file)
    predictions = []
    model = ApiConfig.model
    MLModel.objects.create(file_id=file_object,
                           model_name="Random Forest Regressor",
                           model_score=98.0)
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
            file_id=file_object,
            carat=input_data[0][0],
            cut=ApiConfig.cut_enc.inverse_transform([input_data[0][1].astype(int)])[0],
            color=ApiConfig.color_enc.inverse_transform([input_data[0][2].astype(int)])[0],
            clarity=ApiConfig.clarity_enc.inverse_transform([input_data[0][3].astype(int)])[0],
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
    returnObject = FileSerializer(instance=file_object)

    return returnObject
