from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import LengthRequired

app = Flask(__name__) #built-in variable 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b704e342f5c5a86b41a2606d'
db = SQLAlchemy(app)

from markets import routes

'''
This file responsibles for define the package of folder
'''

