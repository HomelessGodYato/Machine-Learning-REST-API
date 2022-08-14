import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import bz2

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
# scaler = StandardScaler()
# scaler.fit(X)
# X = scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestRegressor()
model.fit(X_train.values, y_train.values)
# print(model.score(X_test,y_test))
joblib.dump(cut_encoder, "./PredictionModelAPI/ml/Encoders/cut_encoder.pkl", compress=3)
joblib.dump(color_enc, "./PredictionModelAPI/ml/Encoders/color_encoder.pkl", compress=3)
joblib.dump(clarity_enc, "./PredictionModelAPI/ml/Encoders/clarity_encoder.pkl", compress=3)
joblib.dump(model, "./PredictionModelAPI/ml/Model/random_forest_regressor.pkl", compress=3)
# with bz2.BZ2File('cut_encoder.pbz2', 'wb') as cut_enc:
#     pickle.dump(cut_encoder, cut_enc)
#
# with bz2.BZ2File('color_encoder.pbz2', 'wb') as color_encoder:
#     pickle.dump(color_enc, color_encoder)
#
# with bz2.BZ2File('clarity_encoder.pbz2', 'wb') as clarity_encoder:
#     pickle.dump(clarity_enc, clarity_encoder)
#
# with bz2.BZ2File('random_forest_regressor.pbz2', 'wb') as rf_cls:
#     pickle.dump(model, rf_cls)
