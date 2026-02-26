from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load the trained model
# model = pickle.load(open('model/schizophrenia_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'eeg_file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['eeg_file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
        
    if file and file.filename.endswith('.edf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Process EEG data
        # In a real scenario, use mne library: raw = mne.io.read_raw_edf(filepath)
        # df = raw.to_data_frame()
        
        # Extract features (mock logic for demonstration)
        # features = extract_features(df)
        
        # Run AI model
        # prediction = model.predict(features)
        # risk_score = model.predict_proba(features)[0][1] * 100
        
        # Mock prediction for demonstration
        risk_score = 75.5
        
        if risk_score > 60:
            risk_level = 'High Risk'
        elif risk_score > 30:
            risk_level = 'Medium Risk'
        else:
            risk_level = 'Low Risk'
            
        return render_template('result.html', 
                               risk_score=risk_score, 
                               risk_level=risk_level)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
