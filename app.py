from flask import Flask, render_template, request, url_for, flash, redirect, jsonify

import pickle
from datetime import datetime
import pandas as pd
from sklearn import datasets
from sqlalchemy import create_engine


app = Flask(__name__)








@app.route('/hola', methods= ["GET"])
def saluda():
    
    return render_template("plantilla.html")  



if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)