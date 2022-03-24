from flask import jsonify
from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('department',required=True)
parser.add_argument('name',required=True)
parser.add_argument('surname',required=True)
parser.add_argument('gender',required=True)

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

    @jwt_required
    def post(self,id):
        data = parser.parse_args()
        data['id'] = id
        try:   
            self.helper.addElement(data)
            return jsonify({'message':'OK'})
        except(e):
            print(e)
            return jsonify({'message':'error'})

    @jwt_required
    def put(self,id):
        data = parser.parse_args()
        data['id'] = id
        try:   
            self.helper.updateElement(data,'id',id)
            return jsonify({'message':'OK'})
        except(e):
            print(e)
            return jsonify({'message':'error'})

    @jwt_required
    def delete(self,id):
        try:
            self.helper.deleteElement("id",id)
            return jsonify({'message':'deleted element with id '+ str(id)})
        except:
            return jsonify({'message':'error'})

class TeachersByDep(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self,dep):
        data = self.helper.getFilteredData('department',dep)
        return jsonify(data)

