from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/spamer')
def spamer():
    return render_template('spamer.html') 


if __name__ == '__main__':
    app.run(debug=True)