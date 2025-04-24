import pickle
from flask import Flask, render_template, request
import sklearn
application = Flask(__name__)
app=application

# Load classifier and scaler
classifier_model = pickle.load(open('models/gradient.pkl', 'rb'))
standard_scaler = pickle.load(open('models\scalar.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predictFire', methods=['GET', 'POST'])
def predictFire():
    result = None

    if request.method == 'POST':
        # Get input data
        data = {
            'Temperature': float(request.form['Temperature']),
            'RH': float(request.form['RH']),
            'Ws': float(request.form['Ws']),
            'Rain': float(request.form['Rain']),
            'FFMC': float(request.form['FFMC']),
            'DMC': float(request.form['DMC']),
            'ISI': float(request.form['ISI']),
            'Region': int(request.form['Region'])
        }

        # Transform input for prediction
        input_features = [[
            data['Temperature'],
            data['RH'],
            data['Ws'],
            data['Rain'],
            data['FFMC'],
            data['DMC'],
            data['ISI'],
            data['Region']
        ]]
        scaled_input = standard_scaler.transform(input_features)

        # Predict
        prediction = classifier_model.predict(scaled_input)[0]
        result = "🔥 Fire Likely" if prediction == 1 else "✅ No Fire Risk"

    return render_template('index.html', result=result)

if __name__=='__main__':
    app.run(debug=True)