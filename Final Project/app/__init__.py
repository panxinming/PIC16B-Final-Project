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

# The function gives us the main page of the Webapp.
@app.route('/', methods=['POST','GET'])

def main():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Preprocessing'))
    return render_template('main.html')


# The function gives us the preprecessing page of the Webapp.
# Call the template preprecssing.html and show preprocessing page.
# If we click on the "next" button, We will jump to feature_selection page
@app.route('/Preprocessing/', methods=['POST','GET'])
def Preprocessing():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Feature_selection'))
    return render_template('Preprocessing.html')


# The function gives us the feature_selection page of the Webapp.
# Call the template preprecssing.html and show feature_selection page.
# If we click on the "next" button, We will jump to Models page
@app.route('/Feature_selection/', methods=['POST','GET'])
def Feature_selection():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Models'))
    return render_template('Feature_selection.html')

# The function gives us the models page of the Webapp.
# Call the template models.html and show models page.
# If we click on the "next" button, We will jump to diagnosis page
@app.route('/Models/', methods=['POST', 'GET'])
def Models():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('Diagnosis'))
    return render_template('Models.html')


# The function gives us the diagnosis page of the Webapp.
# Call the template diagnosis.html and fetch the data we inputted and store them to 
# g.text1,g.text2,g.text3 and g.text4, they are area_worst,area_mean, concave.points_mean
# and concave.points_worst. then we fetch the type of the models we selected and fetch the 
# models which has been trained from //models and then predict whether the The diagnosis of the 
# breast cancer is benign or malignant.
@app.route('/Diagnosis/', methods=['POST', 'GET'])
def Diagnosis():
    if request.method == 'GET':
        return render_template('Diagnosis.html')
    else:
        try:
            # retrieve the image
            g.text1 = float(request.form['text1'])  #area_worst
            g.text2 = float(request.form['text2'])  #area_mean
            g.text3 = float(request.form['text3'])  #concave.points_mean
            g.text4 = float(request.form['text4'])  #concave.points_worst
            #standarize the input data
            X_value = [g.text1,g.text2,g.text3,g.text4]
            df3 = pd.read_csv(".\\files\\standarize.csv")
            c=["mean","std"]
            df4 = df3.loc[:,c]
            X_value= (X_value-df4["mean"])/df4["std"]
            X_value=np.array(X_value).tolist()
            X_value = [X_value]

            g.m = request.form['model']
            if g.m == "LR":    #if you select Logistic Regression
                g.model = joblib.load(".\\models\\LR.m") 
            elif g.m == "DT":  #if you select Decision Tree
                g.model = joblib.load(".\\models\\DT.m")
            elif g.m == "MLP": #if you select MultilayerPerceptron
                g.model = joblib.load(".\\models\\MLP.m")
            elif g.m == "RF":  #if you select Random Forest
                g.model = joblib.load(".\\models\\RF.m")
            elif g.m == "SVM":  #if you select Support Vector Machine
                g.model = joblib.load(".\\models\\SVM.m")
            else:               #if you select Tensor Flow
                g.model = tf.keras.models.load_model(".\\models\\TF")

            #predict the result
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
           