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
2. Compose docker containers
    1. Compose database container:
    ```sh
    docker-compose up db
    ```
    2. Open second terminal and make migrations:
   ```sh
   docker-compose run web python manage.py makemigrations
   ```
    3. Apply all migrations:
   ```sh
   docker-compose run web python manage.py migrate --run-syncdb
   ```
    4. Run web server:
   ```sh
   docker-compose up web
   ```
3. Now API is set up.
4. You can test API via ```api_testing.py``` script.
   1. Just run it from IDE or terminal
   2. You can find all responses inside ```Output Files``` directory.
5. Or use Postman.

   