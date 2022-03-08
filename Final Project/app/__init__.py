# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request, redirect,url_for
import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
import joblib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


app = Flask(__name__)

# Create main page (fancy)

@app.route('/', methods=['POST','GET'])

def main():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Preprocessing'))
    return render_template('main.html')

# Show url matching

@app.route('/Preprocessing/', methods=['POST','GET'])
def Preprocessing():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Feature_selection'))
    return render_template('Preprocessing.html')

# Page with form
@app.route('/Feature_selection/', methods=['POST','GET'])
def Feature_selection():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Models'))
    return render_template('Feature_selection.html')


@app.route('/Models/', methods=['POST', 'GET'])
def Models():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Diagnosis'))
    return render_template('Models.html')


# File uploads and interfacing with complex Python
# basic version

@app.route('/Diagnosis/', methods=['POST', 'GET'])
def Diagnosis():
    if request.method == 'GET':
        return render_template('Diagnosis.html')
    else:
        try:
            # retrieve the image
            g.text1 = float(request.form['text1'])
            g.text2 = float(request.form['text2'])
            g.text3 = float(request.form['text3'])
            g.text4 = float(request.form['text4'])
            #standarize
            X_value = [g.text1,g.text2,g.text3,g.text4]
            df3 = pd.read_csv(".\\files\\standarize.csv")
            c=["mean","std"]
            df4 = df3.loc[:,c]
            X_value= (X_value-df4["mean"])/df4["std"]
            X_value=np.array(X_value).tolist()
            X_value = [X_value]

            g.m = request.form['model']
            if g.m == "LR":
                g.model = joblib.load(".\\models\\LR.m") 
            elif g.m == "DT":
                g.model = joblib.load(".\\models\\DT.m")
            elif g.m == "MLP":
                g.model = joblib.load(".\\models\\MLP.m")
            elif g.m == "RF":
                g.model = joblib.load(".\\models\\RF.m")
            elif g.m == "SVM":
                g.model = joblib.load(".\\models\\SVM.m")
            else:
                g.model = tf.keras.models.load_model(".\\models\\TF")
                        
            if g.m != 'TF':
                g.result = g.model.predict(X_value)[0]
            else:
                g.result = g.model.predict(X_value)[0][1]
            if g.result>0:
                r1 = 1
                r2 = 0
            else:
                r2 = 1
                r1 = 0
            return render_template('Diagnosis.html', result1 = r1, result2 = r2)
        except:
            return render_template('Diagnosis.html', error=True)
           