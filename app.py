from flask import Flask, request, jsonify
from feature_extractor import extract_features
from joblib import load

app = Flask(__name__)
model = load('phishing_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL missing'}), 400

    features = extract_features(url)
    prediction = model.predict([features])[0]
    result = 'Phishing' if prediction == 1 else 'Legitimate'
    return jsonify({'url': url, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
