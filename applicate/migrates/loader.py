#encoding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from applicate.applicate.config.loader import config

app = Flask(__name__)
config = config()

app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']


'''
    使用 mysql 引擎
'''
mysqldb = SQLAlchemy(app)

'''
    使用 mongodb 引擎
'''

def loader():
    return mysqldb