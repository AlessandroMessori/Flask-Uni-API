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

    def post(self):
        return jsonify({'message':'not implemented yet'})

    def put(self):
        return jsonify({'message':'not implemented yet'})

    def delete(self,id):
        self.helper.deleteElement("id",id)
        return jsonify({'message':'deleted element with id '+ str(id)})

class TeachersByDep(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self,dep):
        data = self.helper.getFilteredData('department',dep)
        return jsonify(data)

