import requests
import json
from django.core.files.uploadedfile import SimpleUploadedFile
import os

urls = {
    "upload_file": "http://127.0.0.1:8000/api/rf_cls/json/upload/",
    "all_sent_features": "http://127.0.0.1:8000/api/rf_cls/features/",
    "all_predictions": "http://127.0.0.1:8000/api/rf_cls/predictions/",
    "one_prediction": "http://127.0.0.1:8000/api/rf_cls/prediction/1/"
}

base_path = "./PredictionModelAPI/ml/Data/"

file_name = "test.json"
file_path = os.path.join(base_path, file_name)

with open(file_path, 'rb') as file:
    file_content = file.read()
    file.close()

file_to_upload = SimpleUploadedFile(file_name, file_content)
response_file_upload = requests.post(urls['upload_file'], files={'file': file_to_upload})
response_file_upload_json = json.loads(response_file_upload.text)

response_all_features = requests.get(urls['all_sent_features'])
response_all_features_json = json.loads(response_all_features.text)

response_all_predictions = requests.get(urls['all_predictions'])
response_all_predictions_json = json.loads(response_all_predictions.text)

response_one_prediction = requests.get(urls['one_prediction'])
response_one_prediction_json = json.loads(response_one_prediction.text)

with open("Output_Files/output_file_upload.json", "w") as output_json_file_upload:
    json.dump(response_file_upload_json, output_json_file_upload, indent=4)
    output_json_file_upload.close()

with open("Output_Files/output_file_all_features.json", "w") as output_json_all_features:
    json.dump(response_all_features_json, output_json_all_features, indent=4)
    output_json_all_features.close()

with open("Output_Files/output_file_all_predictions.json", "w") as output_json_all_predictions:
    json.dump(response_all_predictions_json, output_json_all_predictions, indent=4)
    output_json_all_predictions.close()

with open("Output_Files/output_file_one_prediction.json", "w") as output_json_one_prediction:
    json.dump(response_one_prediction_json, output_json_one_prediction, indent=4)
    output_json_one_prediction.close()