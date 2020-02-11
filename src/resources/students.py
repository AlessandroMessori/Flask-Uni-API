from flask import jsonify
from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name',required=True)
parser.add_argument('surname',required=True)
parser.add_argument('gender',required=True)

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

    @jwt_required
    def post(self,id):
        data = parser.parse_args()
        data['mat'] = id
        data['gpa'] = 0
        try:   
            self.helper.addElement(data)
            return jsonify({'message':'OK'})
        except(e):
            print(e)
            return jsonify({'message':'error'})
    
    @jwt_required
    def put(self,id):
        data = parser.parse_args()
        data['mat'] = id
        try:   
            self.helper.updateElement(data,'mat',id)
            return jsonify({'message':'OK'})
        except(e):
            return jsonify({'message':'error'})

    @jwt_required
    def delete(self,id):
        try:
            self.helper.deleteElement("mat",id)
            return jsonify({'message':'deleted student with mat '+ str(id)})
        except:
            return jsonify({'message':'error'})