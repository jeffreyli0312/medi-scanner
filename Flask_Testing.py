import flask
from flask_cors import CORS
from Image_Camera_Upload import *
import cv2
import subprocess
import tkinter as tk
from tkinter import filedialog

from flask import Flask, jsonify, request
from flask_cors import CORS

# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route("/", methods=['GET', 'POST'])
# def home():
#     return render_template('home.html')


# from flask import Flask, render_template, request
# # app = Flask(__name__)
# # @app.route("/", methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         if request.form['submit_button'] == 'Take Picture':
#             take_picture()
#             return render_template('about.html')
#             # pass # do something
#         elif request.form['submit_button'] == 'Upload image':
#             upload_image()
#             return render_template('about.html')
#             # pass # do something else
#         # else:
#         #     pass # unknown
#     # elif request.method == 'GET':
#     # return render_template('home.html')

# if __name__ == '__main__':
#     app.run(debug=True)
#     contact()

from flask import Flask, render_template


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    resp = flask.Response("Foo bar baz")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/')
def index():
  return render_template('home.html')

@app.route('/my-link/') # TAKE PICTURE BUTTON
def my_link():
    print ('I got clicked!')

    (bool, output) = take_picture()

# SHOULD PROBABLY PUT RESULTS HERE ON A NEW PAGE
    if bool:
        return render_template('about.html', output=output)
    return render_template('home.html')

@app.route('/my-link2/') # UPLOAD IMAGE BUTTON
def my_link2(formData):
    print ('I got clicked!')

    (bool, output) = upload_image()

    # output = execute('./script')
    # return render_template('template_name.html',output=output)

    if bool:
        return render_template('about_upload.html', output=(output))
    return render_template('home.html') 

@app.route('/my-link3/') #GOT BACK TO HOME BUTTON
def my_link3():
    print ('I got clicked!')

    # image = upload_image()

# SHOULD PROBABLY PUT RESULTS HERE ON A NEW PAGE
    # return render_template('about.html')
    return render_template('home.html')


    

if __name__ == '__main__':
  app.run(debug=True)
