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
X_test_not_scaled=pd.read_csv("X_test_not_scaled.csv" ,index_col=0)
# t2=t.iloc[:,1:]  #remove extrac col
# pred_prob_hist=[]

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

    # x_input = []
    # for i in range(len(lr_model.feature_names)):
    #
    #     f_value = float(
    #         request.args.get(lr_model.feature_names[i], "0"))
    #     x_input.append(f_value)

    # prediction = "nah"
    #
    # t3=np.array(t2.sample(1))
    # t4=pd.DataFrame(t3)
    # t5=t4.to_html()
    # pred_probs = lr_model.predict_proba(t3).flat
    # pred_prob_hist.append(pred_probs[1])
    # pred_str = ""
    # for class_i in np.argsort(pred_probs)[::-1]:
    #     pred_str += f"""<br>
    #     {lr_model.target_names[class_i]}: {pred_probs[class_i]:g}
    #     """
    t2=t.iloc[:,1:]  #remove extrac col
    sample=t2.sample(1).index[0]
    t3=np.array(t2.iloc[sample]).flatten()
    t4=np.array(t2.sample(1))
    t3_actual=np.array(X_test_not_scaled.iloc[sample])
    d=({"Features":lr_model.feature_names,"Coef":lr_model.coef_.flatten(),
         "Sample_User":t3_actual})
    dict_to_df=pd.DataFrame(d)
    dict_to_df.head()
    dict_to_df_v2=dict_to_df.sort_values(by=['Coef'])
    df_to_html=dict_to_df_v2.to_html()
    pred_probs = lr_model.predict_proba(t4).flat
    pred_str = ""
    for class_i in np.argsort(pred_probs)[::-1]:
        pred_str += f"""<br>
        {lr_model.target_names[class_i]}: {pred_probs[class_i]:g}
        """

    # Return a response with a json in it
    # flask has a quick function for that that takes a dict
    return flask.render_template('predictor.html',
    # prediction=pred_str,
    attrib2=df_to_html,
    prediction=pred_str,
    )

# zzzzzzz cp1

# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:
app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
