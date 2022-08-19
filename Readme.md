# API for diamond price prediction

## Description

API uses pretrained model (Random forest regressor) from scikit-learn package,
for diamond price prediction. Model was trained diamond_prices dataset
from [Kaggle](https://www.kaggle.com/datasets/nancyalaswad90/diamonds-prices).  
Test .json file is inside ```PredictionsModelAPI/ml/Data/``` directory.

## How to use API

1. Clone this repository
    ```sh
   git clone https://github.com/HomelessGodYato/Machine-Learning-REST-API.git
   ```
2. Install requirements
    ```sh
    pip install --upgrade -r requirements.txt
    ```
3. Compose docker containers
    1. Compose database container:
    ```sh
    docker-compose up db
    ```
    2. Open second terminal and make migrations:
   ```sh
   docker-compose run web python manage.py migrate --run-syncdb
   ```
    3. Run web server:
   ```sh
   docker-compose up web
   ```
4. Now API is set up.
5. You can test API via ```api_testing.py``` script.
   1. Just run it from IDE or terminal
   2. You can find all responses inside ```Output Files``` directory.
6. Or use Postman.
## API endpoints
1. ```api/rf_cls/features/``` - gives you list of all features you have sent to ML model.
2. ```api/rf_cls/predictions/``` - gives you list of all predictions that ML model made for your requests.
3. ```api/rf_cls/prediction/<int:pk>/``` - gives you prediction based on id that you provide in endpoint
4. ```api/rf_cls/json/upload/``` - gives you oportunity to upload json file with features for prediction
5. ```api/rf_cls/files/get_all/``` - gives you list of all files you have uploded, features inside those files and predictions made for features. 
## TODO
1. Train and deploy new models.
2. Make possible uploading/training models via API
3. Make possible to do basic data analysis for uploaded file.
4. Make possible to use uploaded .csv file in training chosen model.
