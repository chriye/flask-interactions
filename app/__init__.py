# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request
import sqlite3
#execfile("/PIC16B/flask-interactions/app/app.py")
# import os
# os.system("/PIC16B/flask-interactions/app/app1.py")

#from app1 import insert_message


# import sys
# sys.path.insert(0, '/Desktop/PIC16B/flask-interactions')
# from app1 import insert_message


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


def get_auth_db():
    """
    input  : nothing
    output : a database with a message table
    
    Build a connection to the database. And build a table messages 
    with columns(id, handle, and message)
    """
    # check if message_db in g attribute
    if 'message_db' not in g:
        g.message_db = sqlite3.connect('messages_db.sqlite')

    # check if messages exists in message_db
    cmd = \
            """
            CREATE TABLE IF NOT EXISTS messages(
                id INTEGER,
                handle TEXT,
                message TEXT);
            """
    cursor = g.message_db.cursor()
    cursor.execute(cmd)
    return g.message_db

def insert_message(request):
    """
    input  : a request form that has user input information
    output : nothing

    Add a new row of data into the messages table by SQL command. 
    Each row contains id, handle, and message. 
    id      : the current row number of table add one.
    handle  : the handle given by user
    message : the message given by user
    """


    # connect the database
    g.message_db = get_auth_db()
    cursor = g.message_db.cursor()
    # get the current row number in table messages
    new_cursor = cursor.execute("SELECT * FROM messages;")
    cur_row = new_cursor.fetchall() #current row num
    # modify id
    id = len(cur_row) + 1
    # insert a new row into message table
    cmd = \
        """
        INSERT INTO messages (id, handle, message)
        VALUES ({0}, '{1}', '{2}');
        """.format(id, request.form["handle"], request.form["message"])
    cursor.execute(cmd)
    # run commit to ensure a new row has been saved into messages
    g.message_db.commit()
    g.message_db.close()

# nontrivial version: makes a prediction and shows a viz
@app.route('/submit-advanced/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            insert_message(request)
            return render_template('submit.html', thanks = True,
                                handle = request.form['handle'],
                                message = request.form['message'])
        except:
            return render_template('submit.html', error = True)



def random_messages(n):
    """
    input  : an integer n
    output : random n messages from message_db or fewer if n is
    greater than the total messages that the database has.

    return a collection of n random messages if possible
    """
    # connect the database
    g.message_db = get_auth_db()
    cursor = g.message_db.cursor()
    cmd = \
    """
    SELECT * FROM messages ORDER BY RANDOM() LIMIT {0};
    """.format(n)
    cursor.execute(cmd)
    col = cursor.fetchall()
    g.message_db.close()
    return col; 