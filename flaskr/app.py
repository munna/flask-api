# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from routes import *
# creating a Flask app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# register routes
app.register_blueprint(routes)
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)