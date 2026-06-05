from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")

def extract_features(url):
    url_length = len(url)
    dots = url.count('.')
    https = 1 if url.startswith("https") else 0

    return [[url_length, dots, https]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    features = extract_features(url)
    prediction = model.predict(features)[0]

    result = "Phishing URL, fake website careful" if prediction == 1 else "Legitimate URL, it is Safe"

    return render_template(
        'index.html',
        prediction_text=result
    )

if __name__ == '__main__':
    app.run(debug=True)