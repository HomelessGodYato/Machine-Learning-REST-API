import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('diamond_prices_encoded.csv')

cut_encoder = LabelEncoder()
cut_encoder.fit(data['cut'])
data['cut'] = cut_encoder.transform(data['cut'])

color_enc = LabelEncoder()
color_enc.fit(data['color'])
data['color'] = color_enc.transform(data['color'])

clarity_enc = LabelEncoder()
clarity_enc.fit(data['clarity'])
data['clarity'] = clarity_enc.transform(data['clarity'])
data.to_csv('diamond_prices_encoded.csv')

y = data['price']
X = data.drop(['price'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestRegressor()
model.fit(X_train.values, y_train.values)

joblib.dump(cut_encoder, "./PredictionModelAPI/ml/Encoders/cut_encoder.pkl", compress=3)
joblib.dump(color_enc, "./PredictionModelAPI/ml/Encoders/color_encoder.pkl", compress=3)
joblib.dump(clarity_enc, "./PredictionModelAPI/ml/Encoders/clarity_encoder.pkl", compress=3)
joblib.dump(model, "./PredictionModelAPI/ml/Model/random_forest_regressor.pkl", compress=3)

