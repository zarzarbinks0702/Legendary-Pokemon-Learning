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
logistic_regression_classifications_query = 'SELECT * FROM logistic_regression_classifications'
knn_results_query = 'SELECT * FROM knn_results'
svc_results_query = 'SELECT * FROM svc_results'

random_forest_results = pd.read_sql(random_forest_results_query, conn)
neural_network_results = pd.read_sql(neural_network_results_query, conn)
logistic_regression_results = pd.read_sql(logistic_regression_results_query, conn)
logistic_regression_classifications = pd.read_sql(logistic_regression_classifications_query, conn)
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
@app.route("/randomForest", methods=["GET"])
def randomForestResults():
    random_forest_dict = random_forest_results.to_dict(orient='index')
    return jsonify(random_forest_dict)

@app.route("/neuralNetwork", methods=["GET"])
def neuralNetworkResults():
    neural_network_dict = neural_network_results.to_dict(orient='index')
    return jsonify(neural_network_dict)

@app.route("/logisticRegression", methods=["GET"])
def logisticRegressionResults():
    logistic_regression_dict = logistic_regression_results.to_dict(orient='index')
    return jsonify(logistic_regression_dict)

@app.route("/logisticRegressionClassifications", methods=["GET"])
def logisticRegressionClassifications():
    logistic_regression_class_dict = logistic_regression_classifications.to_dict(orient='index')
    return jsonify(logistic_regression_class_dict)

@app.route("/KNN", methods=["GET"])
def knnResults():
    knn_dict = knn_results.to_dict(orient='index')
    return jsonify(knn_dict)

@app.route("/SVC", methods=["GET"])
def svcResults():
    svc_dict = svc_results.to_dict(orient='index')
    return jsonify(svc_dict)
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
