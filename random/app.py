# app.py

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("random_forest.joblib")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get the input data from the form
        avg_ipt = float(request.form["avg_ipt"])
        bytes_in = float(request.form["bytes_in"])
        # Get other input variables...

        # Make a prediction using the model
        input_data = np.array([[avg_ipt, bytes_in]])  # Add other input variables here
        prediction = model.predict(input_data)

        # Convert the numeric prediction to a human-readable label
        if prediction == 0:
            result = "Outlier"
        elif prediction == 1:
            result = "Malicious"
        else:
            result = "Benign"

        return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
