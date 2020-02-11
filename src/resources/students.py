from flask import jsonify
from flask_restful import Resource

class AllStudents(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self):
        data = self.helper.getData()
        data = sorted(data, key=lambda k: k['mat'])
        return jsonify(data)

class Student(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self,id):
        data = self.helper.getSingleData('mat',id)
        return jsonify(data)
