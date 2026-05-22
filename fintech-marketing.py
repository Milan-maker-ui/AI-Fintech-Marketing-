import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from flask import Flask, request, jsonify
import joblib

data = pd.read_csv(r"C:\Users\arote\OneDrive\Desktop\Fintech-Marketing\fintech_customers (1).csv")
print(data.head())

data.fillna(data.mean(numeric_only=True), inplace = True)

X = data[['Age', 'Income', 'CreditScore', 'Transactions']]
y = data['Response']

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

scaler = StandardScaler()
X_scaler = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split( X_scaler, y, test_size=0.2, random_state= 42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n Accuracy:", accuracy)

print("\n Classification Report:",)
print(classification_report(y_test, y_pred))

joblib.dump(model, "fintech_model.pkl")
joblib.dump(scaler, "scaler.pkl")

app = Flask(__name__)

model = joblib.load("fintech_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.json

    input_data = np.array([[data['Age'], data['Income'], data['CreditScore'], data['Transactions']]])

    input_scaled = scaler_transform(input_data)

    prediction = model.predict(input_scaled)

    result = label_encoder.inverse_transform(prediction)

    return jsonify({"Prediction": result[0]})

if __name__ == "__main__":
    app.run(debug = True)
