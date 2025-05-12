from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Collect input values
            credit_score = float(request.form['CreditScore'])
            age = float(request.form['Age'])
            tenure = float(request.form['Tenure'])
            balance = float(request.form['Balance'])
            num_of_products = float(request.form['NumOfProducts'])
            has_cr_card = float(request.form['HasCrCard'])
            is_active = float(request.form['IsActiveMember'])
            estimated_salary = float(request.form['EstimatedSalary'])

            # One-hot encode Gender
            gender = request.form['Gender']
            gender_male = 1 if gender == 'Male' else 0

            # One-hot encode Geography
            geo = request.form['Geography']
            geo_france = 1 if geo == 'France' else 0
            geo_germany = 1 if geo == 'Germany' else 0
            geo_spain = 1 if geo == 'Spain' else 0

            # Final input vector
            final_input = [
                credit_score, age, tenure, balance,
                num_of_products, has_cr_card, is_active,
                estimated_salary, gender_male,
                geo_france, geo_germany  # geo_spain is implicit (base case)
            ]
            

            # Scale and predict
            input_scaled = scaler.transform([final_input])
            prediction = model.predict(input_scaled)[0]
            result = 'Customer Will Churn' if prediction == 1 else 'Customer Will Not Churn'
        except Exception as e:
            result = f'Error: {str(e)}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
