from flask import jsonify
from flask_restful import Resource

class AllTeachers(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self):
        data = self.helper.getData()
        data = sorted(data, key=lambda k: k['id'])
        return jsonify(data)

class Teacher(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self,id):
        data = self.helper.getSingleData('id',id)
        return jsonify(data)

class TeachersByDep(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self,dep):
        data = self.helper.getFilteredData('department',dep)
        return jsonify(data)