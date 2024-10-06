from flask import Flask, render_template, jsonify
import pandas as pd

# Importing the dataset -------------------------------
file_path = "./gii_countries.csv"
pd.set_option('display.max_columns', None)
try:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
except Exception as e:
    print(f"Error reading the CSV file: {e}")
# -----------------------------------------------------
app = Flask(__name__)
def index():
    return render_template('index.html')
# -----------------------------------------------------

@app.route('/')
def index():
    years = list(range(1990, 2019))  # Adjust according to your data
    gii_data = {year: df[[ 'iso3', 'country', f'gii_{year}']].dropna().to_dict(orient='records') for year in years}

    return render_template('index.html', gii_data=gii_data)

if __name__ == '__main__':
    app.run(debug=True)