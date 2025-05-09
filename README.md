# 🔄 Customer Churn Prediction using Machine Learning

This project predicts whether a customer will **churn** (discontinue the service) based on various attributes like contract type, tenure, internet service, and monthly charges. The model is deployed using **Flask**, providing a simple web interface for real-time predictions.

---

## 📌 Project Overview

Customer churn is a critical metric for subscription-based businesses. This machine learning application helps identify at-risk customers early, enabling companies to take retention measures.

---

## 🛠️ Tech Stack

- **Python**
- **Flask** (for deployment)
- **Scikit-learn**
- **Pandas & NumPy**
- **Matplotlib & Seaborn**
- **Pickle** (for saving the trained model)

---

## 🧠 Workflow

### 1. Data Preprocessing
- Missing value handling
- Categorical encoding:
  - Label Encoding
  - One-Hot Encoding
- Feature Scaling with `StandardScaler`

### 2. Model Training
- Algorithms evaluated:
  - Logistic Regression
  - Random Forest
  - XGBoost
- Metrics used:
  - Accuracy
  - Precision, Recall, F1-Score
  - ROC-AUC

### 3. Deployment
- Best model saved as `churn_model.pkl`
- Flask app with HTML form inputs
- Model loaded to predict churn on user data

---

## 🌐 Web Application Features

- Input customer data through form fields
- Click to get prediction: `Churn` or `Not Churn`
- Clean and responsive interface

---

## 📂 Project Structure

customer-churn/
│
├── templates/ # HTML templates
│ ├── home.html
│ └── result.html
├── static/ # Optional styling
│ └── style.css
├── app.py # Flask backend
├── churn_predictor.py # Data preprocessing and prediction logic
├── churn_model.pkl # Saved ML model
├── requirements.txt
└── README.md

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
2. Install dependencies

pip install -r requirements.txt
3. Start the Flask server

python app.py
Then visit http://localhost:5000 in your browser.

💡 Example Inputs
Feature	Example Value
Gender	Female
Tenure	5
Monthly Charges	70.5
Contract Type	Month-to-month
Internet Service	Fiber optic
Senior Citizen	No
Dependents	Yes

📊 Results & Insights
Random Forest performed best with ~85% accuracy

Most important features: Contract, Tenure, Monthly Charges

Helped derive actionable business insights for customer retention

👨‍💻 Author
Mohammad Mazid
📧 mazidmd750@gmail.com

📜 License
This project is open-source and available under the MIT License.
