# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request

#execfile("/PIC16B/flask-interactions/app/app.py")
# import os
# os.system("/PIC16B/flask-interactions/app/app.py")

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64


# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)

# Create main page (fancy)

@app.route('/')

# def main():
#     return render_template("main.html")

# comment out the below to focus on just the fundamentals

# after running
# $ export FLASK_ENV=development; flask run
# site will be available at 
# http://localhost:5000

def main():
    return render_template('main_better.html')

# Show url matching

# @app.route('/hello/')
# def hello():
#     return render_template('hello.html')



@app.route('/view/')
def view():
    return render_template('view.html')



# @app.route('/hello/<name>/')
# def hello_name(name):
#     return render_template('hello.html', name=name)

# Page with form

# @app.route('/ask/', methods=['POST', 'GET'])
# def ask():
#     if request.method == 'GET':
#         return render_template('submit.html')
#     else:
#         try:
#             return render_template('ask.html', name=request.form['name'], student=request.form['student'])
#         except:
#             return render_template('ask.html')

# File uploads and interfacing with complex Python
# basic version

# @app.route('/submit-basic/', methods=['POST', 'GET'])
# def submit_basic():
#     if request.method == 'GET':
#         return render_template('submit-basic.html')
#     else:
#         try:
#             return render_template('submit-basic.html', thanks = True)
#         except:
#             return render_template('submit-basic.html', error=True)

# nontrivial version: makes a prediction and shows a viz
@app.route('/submit-advanced/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            # insert_message(request)
            return render_template('submit.html', handle = request.form['handle'], message = request.form['message'])
        except:
            return render_template('submit.html', error = True)