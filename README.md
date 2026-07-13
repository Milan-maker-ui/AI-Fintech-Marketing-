# 💳 Fintech Marketing Response Prediction

A Machine Learning project that predicts whether a customer is likely to respond to a fintech marketing campaign based on demographic and financial information. The project also provides a REST API using Flask for real-time predictions.

---

## 📌 Overview

Marketing campaigns are more effective when targeted at customers who are likely to respond. This project uses a **Random Forest Classifier** to predict customer responses based on features such as:

- Age
- Income
- Credit Score
- Number of Transactions

The trained model is deployed using **Flask**, allowing users to send customer data through an API and receive instant predictions.

---

## 🚀 Features

- Data preprocessing and cleaning
- Feature scaling using StandardScaler
- Label encoding for target values
- Random Forest classification model
- Model evaluation with Accuracy Score and Classification Report
- Save trained model using Joblib
- REST API built with Flask
- Easy to extend with new features or datasets

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib

---

## 📊 Dataset

The dataset contains customer information including:

| Feature | Description |
|----------|-------------|
| Age | Customer age |
| Income | Annual income |
| CreditScore | Customer credit score |
| Transactions | Number of transactions |
| Response | Marketing campaign response (Target Variable) |


---

## 🔥 API Endpoint

### POST /predict

#### Request

```json
{
    "Age": 28,
    "Income": 50000,
    "CreditScore": 720,
    "Transactions": 18
}
```

#### Response

```json
{
    "Prediction": "Yes"
}
```

---

## 📈 Model

Algorithm Used:

- Random Forest Classifier

Preprocessing:

- Missing value handling
- Standard Scaling
- Label Encoding

Evaluation Metrics:

- Accuracy Score
- Classification Report

---


## 🔮 Future Improvements

- Hyperparameter tuning
- Feature engineering
- Interactive web dashboard
- Docker deployment
- Cloud deployment (Render, Railway, Azure)
- Model explainability using SHAP
- CI/CD pipeline using GitHub Actions

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---


⭐ If you found this project useful, don't forget to **Star** the repository.
