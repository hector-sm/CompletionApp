from flask import Flask, request, render_template, redirect
import requests
import re
import numpy as np
from sklearn.externals import joblib
import folium

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/data')
def show_data():
    return render_template('data.html')


@app.route('/about')
def show_about():
    return render_template('about.html')


@app.route('/contact')
def show_contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run()
