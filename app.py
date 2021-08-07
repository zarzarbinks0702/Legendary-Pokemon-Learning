from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from os import environ
import sqlite3 as sql
import sys

#init app and class
app = Flask(__name__)

#initiate memory cache of database
conn = sql.connect('Data-and-DBs/pokedex.db')

gen_1_6_query = 'SELECT * FROM gens_1_to_6'
gen_7_query = 'SELECT * FROM gen_7'
gen_8_query = 'SELECT * FROM gen_8'

gen_1_to_6 = pd.read_sql(gen_1_6_query, conn)
gen_7 = pd.read_sql(gen_7_query, conn)
gen_8 = pd.read_sql(gen_8_query, conn)

conn.close()

# Route to render index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getData", methods=["GET"])

####################################
# ADD MORE ENDPOINTS
###########################################

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
