from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

with open("forecast_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    months = int(request.form['months'])
    future = model.make_future_dataframe(periods=months * 30)
    forecast = model.predict(future)
    predictions = forecast[['ds', 'yhat']].tail(months).to_dict(orient='records')
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
