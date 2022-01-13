from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt

app = Flask(__name__) #built-in variable 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b704e342f5c5a86b41a2606d'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from markets import routes

'''
This file responsibles for define the package of folder
'''

