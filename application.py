import pickle
from flask import Flask, render_template, request
import sklearn
application = Flask(__name__)
app = application

# Load classifier and scaler
classifier_model = pickle.load(open(r'C:\Users\mudas\OneDrive\Desktop\ForestFire\models\gradient.pkl', 'rb'))
standard_scaler = pickle.load(open(r'C:\Users\mudas\OneDrive\Desktop\ForestFire\models\scalar.pkl', 'rb'))

@app.route('/')
def home():
<<<<<<< HEAD
    return render_template('Home.html')
=======
    return render_template('Home.html')  # Change to render 'index.html'
>>>>>>> f50ae84d265fa22483aa3e7744102a405fcb4874

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

<<<<<<< HEAD
        # Predict
        prediction = classifier_model.predict(scaled_input)[0]
        result = "🔥 Fire Likely" if prediction == 1 else "✅ No Fire Risk"

    return render_template('index.html', result=result)
=======
        # Make the prediction using the loaded model
        results = ridge_model.predict(scaled_data)
        return render_template('index.html', result=results[0])  # Render 'index.html' with result
    else:
        return render_template('index.html')
>>>>>>> f50ae84d265fa22483aa3e7744102a405fcb4874

if __name__ == '__main__':
    app.run(debug=True)
