# Crime Forecast Application

A web-based application that predicts future crime rates using historical data from Chicago (2012–2017). The application uses Prophet for time series forecasting and provides both visual and tabular representations of predictions.

## Features

- Time series forecasting using Facebook Prophet
- Interactive web interface built with Flask
- Visual representation of forecasts using Chart.js
- Tabular display of predicted values
- Responsive design using Bootstrap

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, JavaScript, Bootstrap
- **Data Analysis**: Prophet, Pandas
- **Visualization**: Chart.js

## Project Structure

```
├── app.py                              # Flask application server
├── forecast.ipynb                      # Jupyter notebook for model development
├── forecast_model.pkl                  # Trained Prophet model
├── Chicago_Crimes_2012_to_2017.xls    # Source data
├── requirements.txt                    # Python dependencies
└── templates
    └── index.html                      # Web interface template
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```
3. Activate the virtual environment:
   ```bash
   myenv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`
3. Enter the number of months you want to forecast
4. View the predictions in both graph and table format

## Dependencies

Key dependencies include:

- Flask 3.1.0
- Prophet 1.1.6
- Pandas 2.2.3
- NumPy 2.2.4
- Chart.js (via CDN)
- Bootstrap 5.3.0 (via CDN)

## Development

The application uses a pre-trained Prophet model saved in `forecast_model.pkl`. The model was developed using historical crime data from Chicago (2012–2017) and can be modified or retrained using the provided Jupyter notebook.
