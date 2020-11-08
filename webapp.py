# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:34:41 2020

@author: rsele
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model_spike = pickle.load(open("model_spike.pkl", "rb"))
model_block = pickle.load(open("model_block.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict_spike',methods=['POST'])

def predict_spike():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model_spike.predict(final_features)

    output_spike = round(prediction[0], 2)
    

    return render_template("index.html", prediction_text_spike="Spike Height should be {} cm ".format(output_spike))


@app.route('/predict_block',methods=['POST'])
def predict_block():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model_block.predict(final_features)

    output_block = round(prediction[0], 2)

    return render_template("index.html", prediction_text_block="Block Height should be {} cm ".format(output_block))




#@app.route("/predict_spike_block",methods=["POST"])
def predict_spike_api():
 
    data = request.get_json(force=True)
    prediction = model_spike.predict([np.array(list(data.values()))])

    output_spike = prediction[0]
    return jsonify_spike(output_spike)


@app.route("/predict_block_api",methods=["POST"])
def predict_block_api():

    data = request.get_json(force=True)
    prediction = model_block.predict([np.array(list(data.values()))])

    output_block = prediction[0]
    return jsonify_block(output_block)

if __name__ == "__main__":
    app.run(debug=True)


