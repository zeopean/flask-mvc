#encoding=utf-8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import loader.config


app = Flask(__name__)
config = loader.config()

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
