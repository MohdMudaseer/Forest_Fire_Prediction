import pickle
from flask import Flask, render_template, request

application = Flask(__name__)
app = application

# Load the pickled models
ridge_model = pickle.load(open(r'C:\Users\mudas\OneDrive\Desktop\ForestFire\models\ridge.pkl', 'rb'))
standard_scaler = pickle.load(open(r'C:\Users\mudas\OneDrive\Desktop\ForestFire\models\scalar.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')  # Change to render 'index.html'

@app.route('/predictFWI', methods=['GET', 'POST'])
def predictFWI():
    result = None  # Default value to ensure result is None initially

    if request.method == 'POST':
        # Get form data
        data = {
            'Temp': float(request.form['Temp']),
            'RH': float(request.form['RH']),
            'Ws': float(request.form['Ws']),
            'Rain': float(request.form['Rain']),
            'FFMC': float(request.form['FFMC']),
            'DMC': float(request.form['DMC']),
            'ISI': float(request.form['ISI']),
            'Classes': int(request.form['Classes']),
            'Region': int(request.form['Region'])
        }

        # Scale the data using the loaded scaler
        scaled_data = standard_scaler.transform([[
            data['Temp'],
            data['RH'],
            data['Ws'],
            data['Rain'],
            data['FFMC'],
            data['DMC'],
            data['ISI'],
            data['Classes'],
            data['Region'] 
        ]])
        print(standard_scaler.n_features_in_)

        # Make the prediction using the loaded model
        results = ridge_model.predict(scaled_data)

    return render_template('index.html', result=results[0])  # Render 'index.html' with result

if __name__ == '__main__':
    app.run(debug=True)
