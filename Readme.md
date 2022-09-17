# API for diamond price prediction

## Description

API uses pretrained models (Random forest regressor, K-Nearest Neighbors) from scikit-learn package,
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
    docker-compose up
    ```
    2. All migrations will apply automatically.
4. Now API is set up.
5. You can test API via ```api_testing.py``` script.
   1. Just run it from IDE or terminal
   2. You can find all responses inside ```Output Files``` directory.
6. Or use Postman.
## API endpoints
1. ```api/features/``` - gives you list of all features you have sent to ML model.
2. ```api/predictions/``` - gives you list of all predictions that ML model made for your requests.
3. ```api/prediction/<int:pk>/``` - gives you prediction based on id that you provide in endpoint
4. ```api/rf_regressor/json/upload/``` - gives you oportunity to upload json file with features for prediction by Random Forest Regressor
5. ```api/knn_regressor/json/upload/``` - same as above, but model is K-Nearest Neighbors.
6. ```api/files/get_all/``` - gives you list of all files you have uploded, features inside those files and predictions made for features.

## Example API response from each endpoint

1. ```api/rf_regressor/json/upload/```  
```json
{
    "id": 2,
    "file": "/test_iaEEf26.json",
    "created": "2022-08-22T09:28:15.819397Z",
    "ml_model": [
        {
            "model_name": "Random Forest Regressor",
            "model_score": 98.0
        }
    ],
    "features": [
        {
            "id": 1,
            "carat": 5.0,
            "cut": "Good",
            "color": "E",
            "clarity": "IF",
            "depth": 61.5,
            "table": 55.0,
            "x": 3.95,
            "y": 3.98,
            "z": 2.43,
            "prediction": [
                {
                    "id": 1,
                    "predicted_price": 12288.8,
                    "features_id": 1
                }
            ]
        },
        {
            "id": 2,
            "carat": 0.23,
            "cut": "Ideal",
            "color": "E",
            "clarity": "IF",
            "depth": 85.4,
            "table": 55.0,
            "x": 3.95,
            "y": 3.98,
            "z": 9.28,
            "prediction": [
                {
                    "id": 2,
                    "predicted_price": 570.9,
                    "features_id": 2
                }
            ]
        },
        {
            "id": 3,
            "carat": 1.2,
            "cut": "Premium",
            "color": "E",
            "clarity": "IF",
            "depth": 61.5,
            "table": 55.0,
            "x": 32.4,
            "y": 3.98,
            "z": 2.43,
            "prediction": [
                {
                    "id": 3,
                    "predicted_price": 11906.2,
                    "features_id": 3
                }
            ]
        }
    ]
}
```

2. ```api/features/```  
```json
[
    {
        "id": 1,
        "carat": 5.0,
        "cut": "Good",
        "color": "E",
        "clarity": "IF",
        "depth": 61.5,
        "table": 55.0,
        "x": 3.95,
        "y": 3.98,
        "z": 2.43,
        "prediction": [
            {
                "id": 1,
                "predicted_price": 13279.03,
                "features_id": 1
            }
        ]
    },
    {
        "id": 2,
        "carat": 0.23,
        "cut": "Ideal",
        "color": "E",
        "clarity": "IF",
        "depth": 85.4,
        "table": 55.0,
        "x": 3.95,
        "y": 3.98,
        "z": 9.28,
        "prediction": [
            {
                "id": 2,
                "predicted_price": 582.45,
                "features_id": 2
            }
        ]
    },
    {
        "id": 3,
        "carat": 1.2,
        "cut": "Premium",
        "color": "E",
        "clarity": "IF",
        "depth": 61.5,
        "table": 55.0,
        "x": 32.4,
        "y": 3.98,
        "z": 2.43,
        "prediction": [
            {
                "id": 3,
                "predicted_price": 13401.338,
                "features_id": 3
            }
        ]
    }
]
```
3. ```api/predictions/```
```json
[
    {
        "id": 1,
        "predicted_price": 13279.03,
        "features_id": 1
    },
    {
        "id": 2,
        "predicted_price": 582.45,
        "features_id": 2
    },
    {
        "id": 3,
        "predicted_price": 13401.338,
        "features_id": 3
    }
]
```
4. ```api/prediction/1/```
```json
{
    "id": 1,
    "predicted_price": 13279.03,
    "features_id": 1
}
```

5. ```api/files/get_all/```
```json
[
    {
        "id": 1,
        "file": "/test_UOIOQxU.json",
        "created": "2022-09-03T16:50:57.173143Z",
        "ml_model": [
            {
                "model_name": "RandomForestRegressor",
                "model_score": 0.98
            }
        ],
        "features": [
            {
                "id": 1,
                "carat": 5.0,
                "cut": "Good",
                "color": "E",
                "clarity": "IF",
                "depth": 61.5,
                "table": 55.0,
                "x": 3.95,
                "y": 3.98,
                "z": 2.43,
                "prediction": [
                    {
                        "id": 1,
                        "predicted_price": 13279.03,
                        "features_id": 1
                    }
                ]
            },
            {
                "id": 2,
                "carat": 0.23,
                "cut": "Ideal",
                "color": "E",
                "clarity": "IF",
                "depth": 85.4,
                "table": 55.0,
                "x": 3.95,
                "y": 3.98,
                "z": 9.28,
                "prediction": [
                    {
                        "id": 2,
                        "predicted_price": 582.45,
                        "features_id": 2
                    }
                ]
            },
            {
                "id": 3,
                "carat": 1.2,
                "cut": "Premium",
                "color": "E",
                "clarity": "IF",
                "depth": 61.5,
                "table": 55.0,
                "x": 32.4,
                "y": 3.98,
                "z": 2.43,
                "prediction": [
                    {
                        "id": 3,
                        "predicted_price": 13401.338,
                        "features_id": 3
                    }
                ]
            }
        ]
    }
]
```

## Postman collection 
 

You can use Postman collection to test API endpoints.  
You will need to install a Postman desktop version to use this tool with your local server. After installation register or log in. Then create new workspace and click on collections button. In your workspace click import button and choose option link then use this link: https://www.getpostman.com/collections/6a123bb8699fda9a1752 Now you are able to test api in a very comfortable way.

