<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Forest Fire Classification</title>
</head>
<body>

  <h1>🌲 Forest Fire Classification - Fire or Not Fire 🔥</h1>

  <h2>📂 Algerian Forest Fires Dataset</h2>
  <p>This project involves building a <strong>classification model</strong> to predict the occurrence of forest fires (<strong>Fire</strong> or <strong>Not Fire</strong>) using the Algerian Forest Fires Dataset. It includes <strong>data cleaning</strong>, <strong>EDA</strong>, <strong>feature engineering</strong>, and <strong>model development</strong>. The project was implemented as part of a Udemy course by <strong>Krish Naik</strong>.</p>

  <h2>📊 Dataset Overview</h2>
  <p>The dataset includes <strong>244 instances</strong> of forest weather data from two regions in Algeria:</p>
  <ul>
    <li><strong>Bejaia Region</strong> (northeast Algeria)</li>
    <li><strong>Sidi Bel-abbes Region</strong> (northwest Algeria)</li>
  </ul>
  <p>Each region contributes 122 instances, covering the period from <strong>June to September 2012</strong>. The dataset is suitable for both regression and classification tasks. This project focuses on the <strong>classification task</strong> — predicting fire occurrence.</p>

  <h2>🧾 Attribute Information</h2>
  <table border="1">
    <tr>
      <th>#</th>
      <th>Feature Name</th>
      <th>Description</th>
      <th>Range</th>
    </tr>
    <tr><td>1</td><td>Date</td><td>Day, Month, Year (DD/MM/YYYY)</td><td>June–September 2012</td></tr>
    <tr><td>2</td><td>Temp</td><td>Noon Temperature (°C)</td><td>22 – 42</td></tr>
    <tr><td>3</td><td>RH</td><td>Relative Humidity (%)</td><td>21 – 90</td></tr>
    <tr><td>4</td><td>Ws</td><td>Wind Speed (km/h)</td><td>6 – 29</td></tr>
    <tr><td>5</td><td>Rain</td><td>Total Daily Rain (mm)</td><td>0 – 16.8</td></tr>
    <tr><td>6</td><td>FFMC</td><td>Fine Fuel Moisture Code</td><td>28.6 – 92.5</td></tr>
    <tr><td>7</td><td>DMC</td><td>Duff Moisture Code</td><td>1.1 – 65.9</td></tr>
    <tr><td>8</td><td>DC</td><td>Drought Code</td><td>7 – 220.4</td></tr>
    <tr><td>9</td><td>ISI</td><td>Initial Spread Index</td><td>0 – 18.5</td></tr>
    <tr><td>10</td><td>BUI</td><td>Buildup Index</td><td>1.1 – 68</td></tr>
    <tr><td>11</td><td>FWI</td><td>Fire Weather Index</td><td>0 – 31.1</td></tr>
    <tr><td>12</td><td>Classes</td><td>Fire occurrence (Target)</td><td>1 = Fire, 0 = Not Fire</td></tr>
  </table>

  <h2>🚀 Project Highlights</h2>
  <ul class="checklist">
    <li>EDA: Visualized distributions, trends, and relationships among features.</li>
    <li>Data Cleaning: Handled missing values, standardized formats, and encoded categorical features.</li>
    <li>Feature Engineering: Created new inputs and normalized features for model training.</li>
    <li>Model Training: Trained a <strong>classification model</strong> (e.g., Gradient Boosting) to predict fire occurrence.</li>
    <li>Deployment: Built a simple <strong>Flask web app</strong> for fire occurrence prediction based on user inputs.</li>
  </ul>

  <h2>🎓 Learning Acknowledgement</h2>
  <p>This project was built while following the <strong>Machine Learning course by Krish Naik</strong> on Udemy. It helped me gain hands-on experience with classification problems, web deployment, and end-to-end ML workflows.</p>

</body>
</html>
