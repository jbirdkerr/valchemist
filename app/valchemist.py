import os
import flask
from flask import Flask, render_template
from flask import Blueprint
from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required

from models import db, User, Role

from flask import request
import json

from time import sleep
from datetime import datetime
import hashlib
import random
import uuid

__author__ = "Prahlad Yeri"
__version__ = "1.2"

app = Flask(__name__, static_url_path='', static_folder='static')
#app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'upload'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['MONGODB_DB'] = 'valchemist'
app.config['MONGODB_HOST'] = 'localhost'

app.config['SECRET_KEY'] = 'l33tN3rdz'

db.init_app(app)

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)



@app.route("/")
def home():

    return render_template('index.html')

if __name__ == "__main__":
	#print 'DEBUG: ' + str(models.DEBUG)
	app.run(debug=True)