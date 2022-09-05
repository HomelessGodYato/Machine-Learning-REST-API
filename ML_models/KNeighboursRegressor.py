import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

data = pd.read_csv('./Dataset/diamond_prices.csv')

copied_data = data.copy()

cut_enc = LabelEncoder()
data['cut'] = cut_enc.fit_transform(data['cut'])


color_enc = LabelEncoder()
data['color'] = color_enc.fit_transform(data['color'])

clarity_enc = LabelEncoder()
data['clarity'] = clarity_enc.fit_transform(data['clarity'])

y = data['price']
X = data.drop(['price'], axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = KNeighborsRegressor()
model.fit(X_train.values, y_train.values)
model_accuracy = model.score(X_test.values, y_test.values)

# can be deleted
joblib.dump(cut_enc, "../PredictionModelAPI/ml/Encoders/cut_encoder.pkl", compress=3)
joblib.dump(color_enc, "../PredictionModelAPI/ml/Encoders/color_encoder.pkl", compress=3)
joblib.dump(clarity_enc, "../PredictionModelAPI/ml/Encoders/clarity_encoder.pkl", compress=3)
joblib.dump(model, f"../PredictionModelAPI/ml/Model/{type(model).__name__}.pkl", compress=3)
joblib.dump(model_accuracy, f"../PredictionModelAPI/ml/Scores/{type(model).__name__}_score.pkl", compress=3)

