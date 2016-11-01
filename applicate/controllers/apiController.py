#encoding=utf-8
from flask import Flask
from flask import render_template,flash,redirect,request
from flask import jsonify
from applicate import app
import applicate.record as record

@app.route('/api', methods=['get'])
def index():
    return jsonify({
        'code':'zeopean',
        'message':'hello zeopean'
    })

@app.route('/api-get-model', methods=['get'])
def get_model():

    user = record.getUser()
    if(user):
        return jsonify({
            'code':'1',
            'message':'success'
        })
