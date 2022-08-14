import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import os
import bz2

data = pd.read_csv('diamond_prices.csv')

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
model.fit(X_train, y_train)
# print(model.score(X_test,y_test))
# pickle.dump(cut_encoder, open('cut_encoder.pkl', 'wb'))
# pickle.dump(color_enc, open('color_encoder.pkl', 'wb'))
# pickle.dump(clarity_enc, open('clarity_encoder.pkl', 'wb'))
pickle.dump(model, open('random_forest_regressor.pkl', 'wb'))
compressed_model = bz2.BZ2File("random_forest_regressor_compressed.pkl", 'wb')
pickle.dump(model, compressed_model)
# print(os.path.getsize("random_forest_regressor_compressed.pkl"))
