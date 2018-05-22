import flask
from flask import request
import pickle
import numpy as np
import pandas as pd
import random

# Initialize the app
app = flask.Flask(__name__)
with open("lr_dest.pkl","rb") as f:
    lr_model = pickle.load(f)


t=pd.read_csv("X_test_for_testing.csv")
t2=t.iloc[:,1:]


# lr_model.feature_names = ["blah", "blah1", "blah2"]

# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!

@app.route("/")
def hello():
    return "It's alive22!!!"


# Let's turn this into an API where you can post input data and get
# back output data after some calculations.

# If a user makes a POST request to http://127.0.0.1:5000/predict, and
# sends an X vector (to predict a class y_pred) with it as its data,
# we will use our trained LogisticRegression model to make a
# prediction and send back another JSON with the answer. You can use
# this to make interactive visualizations.

@app.route("/predict", methods=["POST", "GET"])
def predict():

    x_input = []
    for i in range(len(lr_model.feature_names)):

        f_value = float(
            request.args.get(lr_model.feature_names[i], "0"))
        x_input.append(f_value)

    # prediction = "nah"


    pred_probs = lr_model.predict_proba([x_input]).flat

    pred_str = ""
    for class_i in np.argsort(pred_probs)[::-1]:
        pred_str += f"""<br>
        {lr_model.target_names[class_i]}: {pred_probs[class_i]:g}
        """


    # Return a response with a json in it
    # flask has a quick function for that that takes a dict
    return flask.render_template('predictor.html',
    feature_names=lr_model.feature_names,
    x_input=x_input,
    prediction=pred_str
    )



# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:
app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
