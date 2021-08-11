from flask import Flask, render_template, jsonify, request
import json
import pandas as pd
import numpy as np
import sqlite3 as sql

#init app and class
app = Flask(__name__)

#initiate memory cache of database
conn = sql.connect('Data-and-DBs/pokedex.db')

random_forest_results_query = 'SELECT * FROM random_forest_results'
neural_network_results_query = 'SELECT * FROM neural_network_results'
logistic_regression_results_query = 'SELECT * FROM logistic_regression_results'
knn_results_query = 'SELECT * FROM knn_results'
svc_results_query = 'SELECT * FROM svc_results'

random_forest_results = pd.read_sql(random_forest_results_query, conn)
neural_network_results = pd.read_sql(neural_network_results_query, conn)
logistic_regression_results = pd.read_sql(logistic_regression_results_query, conn)
knn_results = pd.read_sql(knn_results_query, conn)
svc_results = pd.read_sql(svc_results_query, conn)

conn.close()

# Route to render index.html template
@app.route("/")
def home():
    return render_template("index.html")

####################################
# ADD MORE ENDPOINTS
###########################################
@app.route("/randomTree", methods=["GET"])
def randomTreeResults():
    return jsonify(random_forest_results)

@app.route("/neuralNetwork", methods=["GET"])
def randomTreeResults():
    return jsonify(neural_network_results)

@app.route("/logisticRegression", methods=["GET"])
def randomTreeResults():
    return jsonify(logistic_regression_results)

@app.route("/KNN", methods=["GET"])
def randomTreeResults():
    return jsonify(knn_results)

@app.route("/SVC", methods=["GET"])
def randomTreeResults():
    return jsonify(svc_results)
#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
