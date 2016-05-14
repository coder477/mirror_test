'''
Created on May 14, 2016

@author: Sneha
'''
import os
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
     
    return render_template('mirror.html')

@app.route('/return_page', methods=['POST'])    
def return_page():
    name=request.form['yourtext']
    print name
    return render_template('mirror.html',entered=name)
if __name__ == "__main__":
    app.run()