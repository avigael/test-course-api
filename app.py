from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)

CORS(app)

try:
    with open('class_data.json','r') as filedata:
            COURSES = json.load(filedata)
    with open('class_data_previous.json','r') as filedata:
            PREV_COURSES = json.load(filedata)
except Exception as e:
    print('Error loading json data: '+str(e))
    COURSES = {}
    PREV_COURSES = {}

@app.route('/courses/completed/',methods=['GET'])
def get_completed():
    return PREV_COURSES

@app.route('/courses/',methods=['GET'])
def get_classes():
    return COURSES

if __name__ == '__main__':
    app.run(debug=False)
